import os
import shutil
import time
from PIL import Image, UnidentifiedImageError
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog
from eyed3 import id3
from mutagen import File
import tempfile


def sanitize_filename(filename):
    return "".join(
        c if c.isalnum() or c in [".", "_", "-", " "] else "_" for c in filename
    )


def get_album_tag(file_path):
    if file_path.endswith(".mp3"):
        audio = id3.Tag()
        audio.parse(file_path)
        return audio.album
    elif file_path.endswith(".flac"):
        try:
            audio = File(file_path)
            album_tag = audio.get("album")
            return album_tag[0] if isinstance(album_tag, list) else album_tag
        except Exception as e:
            print(f"Error reading FLAC metadata for {file_path}: {e}")
            return None


def organize_music_files(root_dir):
    for filename in os.listdir(root_dir):
        file_path = os.path.join(root_dir, filename)

        if os.path.isfile(file_path) and file_path.endswith((".mp3", ".flac")):
            album_tag = get_album_tag(file_path)

            if album_tag:
                sanitized_album_tag = sanitize_filename(str(album_tag))
                album_folder = os.path.join(root_dir, sanitized_album_tag)
                if not os.path.exists(album_folder):
                    os.makedirs(album_folder)

                try:
                    shutil.move(file_path, os.path.join(album_folder, filename))
                    print(f"Moved '{filename}' to '{sanitized_album_tag}' folder.")
                except Exception as e:
                    print(
                        f"Error moving '{filename}' to '{sanitized_album_tag}' folder: {e}"
                    )

                time.sleep(0.1)


def extract_cover_ffmpeg(directory, temp_folder):
    print(f"\nChecking directory: {directory}")
    files = os.listdir(directory)

    if "cover.jpg" in files:
        print(f"Cover image found in {directory}")
    else:
        image_files = [
            file for file in files if file.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        if image_files:
            print("Image files found in the directory:")
            for i, image_file in enumerate(image_files, start=1):
                print(f"{i}. {image_file}")

            selected_index = (
                int(
                    input(
                        "Enter the number of the image file you want to use as the cover image: "
                    )
                )
                - 1
            )
            selected_image_file = image_files[selected_index]

            cover_dest_path = os.path.join(directory, "cover.jpg")
            shutil.move(os.path.join(directory, selected_image_file), cover_dest_path)
            print(f"Selected image file '{selected_image_file}' set as cover image.")

            # Delete other image files
            for image_file in image_files:
                if image_file != selected_image_file:
                    os.remove(os.path.join(directory, image_file))
                    print(f"Deleted redundant image file '{image_file}'.")

        else:
            flac_files = [file for file in files if file.endswith(".flac")]
        mp3_files = [file for file in files if file.endswith(".mp3")]

        if flac_files:
            flac_file_path = os.path.join(directory, flac_files[0])
            temp_folder_path = os.path.join(temp_folder, "cover_extraction_temp")

            try:
                os.makedirs(temp_folder_path, exist_ok=True)

                encoding = sys.stdout.encoding or "utf-8"
                temp_cover_path = os.path.join(temp_folder_path, "cover.jpg")
                print(f"Running ffmpeg command for '{flac_file_path}'")
                result = subprocess.run(
                    ["ffmpeg", "-i", flac_file_path, temp_cover_path],
                    text=True,
                    capture_output=True,
                    encoding=encoding,
                )

                print(f"\nffmpeg command output: {result.stdout}")
                print(f"ffmpeg command error: {result.stderr}")

                if result.returncode == 0:
                    cover_dest_path = os.path.join(directory, "cover.jpg")
                    shutil.move(temp_cover_path, cover_dest_path)
                    print(
                        f"FLAC Cover image extracted and saved as baseline JPEG in {directory}"
                    )
            except Exception as e:
                print(f"Error during extraction: {e}")
            finally:
                pass

        elif mp3_files:
            mp3_file_path = os.path.join(directory, mp3_files[0])
            temp_folder_path = os.path.join(temp_folder, "cover_extraction_temp")

            try:
                os.makedirs(temp_folder_path, exist_ok=True)

                encoding = sys.stdout.encoding or "utf-8"
                temp_cover_path = os.path.join(temp_folder_path, "cover.jpg")
                print(f"Running ffmpeg command for '{mp3_file_path}'")
                result = subprocess.run(
                    ["ffmpeg", "-i", mp3_file_path, temp_cover_path],
                    text=True,
                    capture_output=True,
                    encoding=encoding,
                )

                print(f"\nffmpeg command output: {result.stdout}")
                print(f"ffmpeg command error: {result.stderr}")

                if result.returncode == 0:
                    cover_dest_path = os.path.join(directory, "cover.jpg")
                    shutil.move(temp_cover_path, cover_dest_path)
                    print(
                        f"MP3 Cover image extracted and saved as baseline JPEG in {directory}"
                    )
            except Exception as e:
                print(f"Error during extraction: {e}")
            finally:
                pass


def restore_backups(root_dir):
    print("\nRestoring backups...")
    for root, dirs, files in os.walk(root_dir):
        if ".rockbox" in dirs:
            dirs.remove(".rockbox")

        for file in files:
            if file.lower().endswith((".jpg.backup", ".jpeg.backup", ".png.backup")):
                backup_path = os.path.join(root, file)
                original_filename = sanitize_filename(file[:-7])
                original_path = os.path.join(root, original_filename)

                if os.path.exists(backup_path):
                    shutil.move(backup_path, original_path)
                    print(f"Restored: '{original_filename}'")
                else:
                    print(f"Backup not found for: '{original_filename}'")


def process_images(root_dir, iteration_timeout=5, max_retries=3):
    retries = 0
    processed_folders = set()
    try:
        while retries <= max_retries:
            folders_processed = 0

            for root, dirs, files in os.walk(root_dir):
                if ".rockbox" in dirs:
                    dirs.remove(".rockbox")

                cover_path = os.path.join(root, "cover.jpg")

                if root in processed_folders:
                    continue

                if os.path.exists(cover_path) and os.path.getsize(cover_path) > 0:
                    print(f"\nProcessing folder: {root}")

                    try:
                        with Image.open(cover_path) as img:
                            if img.mode in ("RGBA", "LA"):
                                img = img.convert("RGB")

                            if img.size != (200, 200):
                                img = img.resize((200, 200))
                                img.save(cover_path, "JPEG", quality=95, subsampling=0)
                                print(f"Modified 'cover.jpg' in {root}")
                            else:
                                print(
                                    "'cover.jpg' is already a baseline JPEG with dimensions 200x200. Skipping."
                                )

                    except UnidentifiedImageError as e:
                        print(f"Error processing 'cover.jpg': {str(e)}")
                        continue

                else:
                    extract_cover_ffmpeg(
                        root,
                        os.path.join(tempfile.gettempdir(), "cover_extraction_temp"),
                    )
                    folders_processed += 1
                    processed_folders.add(root)

            if folders_processed > 0:
                print(f"\n{folders_processed} folder(s) processed.")
                retries = 0
            else:
                print("\nNo folders to process. Exiting.")
                break

            time.sleep(iteration_timeout)

    except KeyboardInterrupt:
        print("\nProcessing interrupted by user.")


def clear_temp_directory():
    temp_folder = os.getenv("TEMP")
    temp_folder_path = os.path.join(
        temp_folder, "cover_extraction_temp", "cover_extraction_temp"
    )

    if os.path.exists(temp_folder_path):
        shutil.rmtree(temp_folder_path)
        print(f"Cleared directory: {temp_folder_path}")
    else:
        print(f"Directory does not exist: {temp_folder_path}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    root_directory = filedialog.askdirectory(title="Select Root Directory")

    if not root_directory:
        print("\nNo directory selected. Exiting.")
    else:
        restore_backups(root_directory)
        organize_music_files(root_directory)
        process_images(root_directory)
