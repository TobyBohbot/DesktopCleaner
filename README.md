# DesktopCleaner

This Python script automatically organizes files in your Downloads directory into specific folders based on file type. The script monitors the `Downloads` folder and moves files into predefined directories such as Music, Videos, Images, and Documents.

## Features

- **Automated File Organization**: Automatically moves files to the correct directories based on their extensions.
- **Supported File Types**: Handles audio, video, image, and document files with customizable file extensions.
- **Customizable Paths**: You can easily customize the source directory and destination directories.
- **Unique File Names**: Ensures that files with the same name are not overwritten by appending a counter to the filename.

## Prerequisites

- Python 3.x
- Required Python packages:
    - `watchdog`

## Installation

1. **Clone the repository** (or create the script file manually):
    ```bash
    git clone https://github.com/yourusername/file-organizer.git
    cd file-organizer

2. **Install the required Python packages**:
    ```bash
    pip install watchdog

3. **Update the script with your paths**:

- Open "**file_organizer.py**".
- Update the paths in the script to match your directory structure:
    ```bash
    source_dir = "/path/to/your/source"
    dest_dir_sfx = "/path/to/your/sfx"
    dest_dir_music = "/path/to/your/music"
    dest_dir_video = "/path/to/your/videos"
    dest_dir_image = "/path/to/your/images"
    dest_dir_documents = "/path/to/your/documents"

## Usage

1. **Run the Script**:

    ```bash
    python file_organizer.py
   
2. Automatic File Handling:
- The script will now monitor the Downloads directory for any new or modified files and will move them to the appropriate directory based on their extension.
3. Stop the Script:
- To stop the script, simply press "**Ctrl + C**" in the terminal.