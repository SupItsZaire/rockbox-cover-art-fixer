# rockbox-cover-art-fixer
A Python script to help with Rockbox cover art conversion.
## WINDOWS ONLY AT THE MOMENT, THIS MIGHT CHANGE YOUR FOLDER STRUCTURES IF YOUR ALBUMS AREN'T SORTED INTO FOLDERS

This script organizes files based on album tags, extracts the cover image out of MP3 and FLAC files using ffmpeg and converts them to a 200x200 baseline .jpg in its respective directory.

## Overview

- **FLAC Cover Extraction:** Extracts cover images embedded in FLAC files and saves them as JPEGs.
- **MP3 Album Cover Processing:** Retrieves album cover information from MP3 files and processes them.
- **Standardized Cover Images:** Ensures cover images are in a standardized format (e.g., baseline JPEG, 200x200 pixels).

## Prerequisites

- Python 3.x
- FFmpeg installed and added to the system PATH
- Required Python packages: `Pillow`, `eyed3`, `mutagen`

## Installation

```bash
pip install Pillow eyed3 mutagen
```
Install FFmpeg. You can download it from the official [FFmpeg website](https://www.ffmpeg.org/).

git clone https://github.com/SupItsZaire/rockbox-cover-art-fixer.git

cd rockbox-cover-art-fixer

## Usage

Run the script with the command:
```bash
python rockboxalbumfix.py
```
Select the root directory containing your music folders using the file dialog.

The script will process the folders, extract cover art, and organize the music files.

## BEST WAY TO USE THIS
just chuck all of your flacs and mp3 into one folder. the script just organizes it neatly in folders :D

## KNOWN ISSUES

- script WILL ignore any png or differnt filetype cover images, fix is on the way soonish
- script might break as i have had no one test this yet aside from me :D
- script loops, just ctrl - c
