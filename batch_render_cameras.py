# MIT License
# 
# Copyright (c) 2024 Rubiel <rubiel@rubielgames.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

bl_info = {
    "name": "Batch Render Cameras",
    "author": "Rubiel (rubiel@rubielgames.com)",
    "version": (1, 0),
    "blender": (4, 2, 0),
    "location": "Render > Batch Render Cameras",
    "description": "Renders all visible cameras and saves images to a timestamped directory",
    "category": "Render",
}

import bpy
import os
import time
from datetime import datetime

class BatchRenderCamerasOperator(bpy.types.Operator):
    """Batch Render Cameras"""
    bl_idname = "render.batch_render_cameras"
    bl_label = "Batch Render Cameras"
    bl_description = "Renders all visible cameras and saves images to a timestamped directory"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Define properties
    output_dir: bpy.props.StringProperty(
        name="Base Output Directory",
        description="Base directory where images will be saved",
        default="d:/Renders/",
        subtype='DIR_PATH',
    )
    
    def execute(self, context):
        # Set the base output directory
        base_output_dir = self.output_dir
        if not base_output_dir:
            self.report({'ERROR'}, "No output directory specified.")
            return {'CANCELLED'}
        
        # Get the current date and time
        current_datetime = datetime.now().strftime('%Y%m%d-%H%M%S')
        
        # Create the subdirectory name
        sub_dir_name = f'cameras-{current_datetime}'
        
        # Combine the base directory and subdirectory
        output_dir = os.path.join(base_output_dir, sub_dir_name)
        
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Print the output directory for verification
        self.report({'INFO'}, f"Images will be saved to: {output_dir}")
        print(f"Images will be saved to: {output_dir}")
        
        # Get the current scene
        scene = context.scene
        
        # Save the original camera
        original_camera = scene.camera
        
        # Get a list of all cameras that are not hidden from render
        cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA' and not obj.hide_render]
        total_cameras = len(cameras)
        
        # Check if there are cameras to render
        if total_cameras == 0:
            self.report({'WARNING'}, "No visible cameras to render.")
            return {'CANCELLED'}
        else:
            # Access the window manager for progress functions
            wm = context.window_manager
            wm.progress_begin(0, total_cameras)
        
            # Record the start time
            start_time = time.time()
        
            try:
                for idx, cam in enumerate(cameras):
                    # Update progress
                    wm.progress_update(idx)
                    print(f"Rendering camera {idx + 1} of {total_cameras}: {cam.name}")
            
                    # Set the scene camera
                    scene.camera = cam
            
                    # Set the render filepath
                    scene.render.filepath = os.path.join(output_dir, cam.name + '.png')
            
                    # Render and save
                    bpy.ops.render.render(write_still=True)
            
                    # Timing calculations
                    elapsed_time = time.time() - start_time
                    average_time = elapsed_time / (idx + 1)
                    remaining_time = average_time * (total_cameras - idx - 1)
                    print(f"Elapsed Time: {elapsed_time:.2f}s, Estimated Remaining Time: {remaining_time:.2f}s")
            except Exception as e:
                self.report({'ERROR'}, f"An error occurred: {e}")
                print(f"An error occurred: {e}")
            finally:
                # End progress
                wm.progress_end()
                print("Rendering complete.")
        
                # Restore original camera
                scene.camera = original_camera
        
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    
def menu_func(self, context):
    self.layout.operator(BatchRenderCamerasOperator.bl_idname)

def register():
    bpy.utils.register_class(BatchRenderCamerasOperator)
    bpy.types.TOPBAR_MT_render.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(BatchRenderCamerasOperator)
    bpy.types.TOPBAR_MT_render.remove(menu_func)
    
if __name__ == "__main__":
    register()
