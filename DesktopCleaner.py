from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the source and destination directories
source_dir = "/Users/Username/Downloads"
dest_dir_sfx = "/Users/Username/Documents/SFX"
dest_dir_music = "/Users/Username/Documents/Music"
dest_dir_video = "/Users/Username/Documents/Videos"
dest_dir_image = "/Users/Username/Documents/Images"
dest_dir_documents = "/Users/Username/Documents/Files"

# Supported file extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".heif", ".heic"]
video_extensions = [".webm", ".mpg", ".mpeg", ".mp4", ".avi", ".mov", ".flv"]
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".aac"]
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# def create_directories():
#     directories = [dest_dir_sfx, dest_dir_music, dest_dir_video, dest_dir_image, dest_dir_documents]
#
#     for directory in directories:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#             print(f"Created directory: {directory}")
#
# # Call the function to create the directories
# create_directories()

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # If file exists, adds a number to the end of the filename
    while exists(join(dest, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)
    move(entry.path, join(dest, name))

class MoverHandler(FileSystemEventHandler):
    # This function will run whenever there is a change in "source_dir"
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():
                    name = entry.name
                    self.check_audio_files(entry, name)
                    self.check_video_files(entry, name)
                    self.check_image_files(entry, name)
                    self.check_document_files(entry, name)

    def check_audio_files(self, entry, name):  # Checks all audio files
        for audio_extension in audio_extensions:
            if name.lower().endswith(audio_extension):
                dest = dest_dir_sfx if entry.stat().st_size < 10_000_000 or "SFX" in name else dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")
                break

    def check_video_files(self, entry, name):  # Checks all video files
        for video_extension in video_extensions:
            if name.lower().endswith(video_extension):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")
                break

    def check_image_files(self, entry, name):  # Checks all image files
        for image_extension in image_extensions:
            if name.lower().endswith(image_extension):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")
                break

    def check_document_files(self, entry, name):  # Checks all document files
        for document_extension in document_extensions:
            if name.lower().endswith(document_extension):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")
                break

# Entry point of the script
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(message)s",
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

































