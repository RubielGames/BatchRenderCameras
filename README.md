# Batch Render Cameras Addon for Blender

## Overview

The **Batch Render Cameras** addon for Blender allows you to automate the rendering process of multiple cameras within your scene. It renders all visible cameras (those not hidden from rendering) and saves the images to a timestamped directory. This addon is especially useful for projects requiring multiple camera angles or perspectives to be rendered efficiently.

## Features

- Renders all visible cameras in the scene.
- Saves rendered images to a subdirectory named `cameras-<datetime>` for easy organization.
- Accessible directly from Blender's **Render** menu.

## Installation

Follow the steps below to install the **Batch Render Cameras** addon in Blender:

### 1. Download the Addon Script

- **Save** `batch_render_cameras.py` on your machine.

### 2. Install the Addon in Blender

1. **Open Blender**.
2. **Go to** `Edit` > **Preferences**.
3. **Select** the **Add-ons** tab on the left panel.
4. **Click** on the **Install...** button located at the top of the window.
5. **Navigate** to where you saved `batch_render_cameras.py` and select it.
6. **Click** **Install Add-on**.
7. After installation, the addon should appear in the list with a checkbox next to it.
8. **Enable** the addon by checking the box next to its name.
9. **Save Preferences** (optional) to keep the addon enabled in future sessions.

## Usage

### Accessing the Addon

1. **Open your Blender project** that contains multiple cameras.
2. **Ensure** that the cameras you want to render are not hidden from rendering (the camera icon in the Outliner is enabled).

### Running the Addon

1. **Go to** the **Render** menu located at the top of the Blender interface.
2. **Select** **Batch Render Cameras...** from the dropdown menu.

### Setting the Output Directory

1. A dialog box titled **Batch Render Cameras** will appear.
2. **Set** the **Base Output Directory**:
   - **Click** on the folder icon next to the input field.
   - **Navigate** to the directory where you want the rendered images to be saved.
   - **Select** the directory and **click** **Accept**.
3. **Confirm** that the path is correct in the input field.

### Starting the Render

1. **Click** **OK** to start the rendering process.
2. The addon will:
   - Create a subdirectory named `cameras-<datetime>` inside the base output directory.
   - Render each visible camera and save the images into the subdirectory.

### Monitoring the Rendering Process

- **Progress Bar**:
  - A progress bar will appear in Blender's status bar, indicating the rendering progress.
- **Console Output**:
  - Detailed information about the rendering process will be printed in the system console.
  - To view the console output:
    - **Windows**:
      - Go to `Window` > **Toggle System Console**.
    - **macOS and Linux**:
      - Run Blender from the terminal to see the console output.

### Viewing the Rendered Images

1. After the rendering is complete, **navigate** to your specified output directory.
2. **Open** the subdirectory named `cameras-<datetime>`, where `<datetime>` corresponds to the date and time when the rendering was initiated.
3. **View** your rendered images, which are named after the cameras.

## Additional Information

### Camera Visibility

- Only cameras that are **visible in the render** (i.e., their **camera icon** in the Outliner is enabled) will be included.
- To exclude a camera from the batch render:
  - **Disable** the camera's render visibility by clicking the **camera icon** next to it in the Outliner.

### Render Settings

- Before running the addon, **configure your render settings** (resolution, samples, output format, etc.) in the **Render Properties** panel.
- The addon uses the current scene's render settings for all cameras.

### Customizing Image Format

- By default, images are saved as `.png` files.
- To change the image format:
  - **Modify** the addon code where the file extension is specified.
    ```python
    scene.render.filepath = os.path.join(output_dir, cam.name + '.png')
    ```
  - Replace `'.png'` with your desired format (e.g., `'.jpg'`, `'.exr'`).

### Date and Time Format

- The subdirectory is named using the current date and time in the format `YYYYMMDD-HHMMSS`.
- To customize the format:
  - **Modify** the following line in the addon code:
    ```python
    current_datetime = datetime.now().strftime('%Y%m%d-%H%M%S')
    ```
  - Refer to Python's `strftime` directives to adjust the format.

### Error Handling

- The addon includes error handling to notify you of any issues during the rendering process.
- Error messages will appear in Blender's status bar and the system console.

## Uninstallation

If you wish to uninstall the addon:

1. **Go to** `Edit` > **Preferences** > **Add-ons**.
2. **Search** for "Batch Render Cameras" in the search bar.
3. **Uncheck** the box next to the addon name to disable it.
4. **Click** the **Remove** button to uninstall the addon from Blender.

## Troubleshooting

- **Addon Not Appearing in Render Menu**:
  - Ensure that the addon is enabled in the Preferences.
  - Restart Blender if necessary.
- **Permission Issues**:
  - Make sure Blender has write permissions to the specified output directory.
- **No Cameras Rendered**:
  - Verify that your cameras are not hidden from rendering.
  - Check that there are cameras in your scene.
- **Console Output Not Visible**:
  - On Windows, toggle the system console via `Window` > **Toggle System Console**.
  - On macOS and Linux, run Blender from the terminal to see console messages.


## License

This addon is provided under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute it as per the license terms.

## Acknowledgments

- **Blender Foundation**: For creating and maintaining Blender.
