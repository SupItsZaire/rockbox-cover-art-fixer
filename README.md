![Archived](https://img.shields.io/badge/status-archived-lightgrey?style=for-the-badge)
[![Moved to Codeberg](https://img.shields.io/badge/moved%20to-Codeberg-2185d0?style=for-the-badge\&logo=codeberg)](https://codeberg.org/supitszaire/rockbox-cover-art-fixer)

# rockbox-cover-art-fixer
A Python script to help with Rockbox cover art conversion.

> ⚠️ **This repository is archived and read-only.**
> Development has been moved to **Codeberg** for the forseeable future:
> https://codeberg.org/supitszaire/rockbox-cover-art-fixer
>
> The move was made due to GitHub platform changes (including CI costs and other ecosystem decisions that I do not endorse or like).
> Please use the Codeberg version for the latest code, issues, and contributions.

## WINDOWS ONLY AT THE MOMENT, THIS MIGHT CHANGE YOUR FOLDER STRUCTURES IF YOUR ALBUMS AREN'T SORTED INTO FOLDERS

This script organizes files based on album tags, extracts the cover image out of MP3 and FLAC files using ffmpeg and converts them to a 200x200 baseline .jpg in its respective directory.

## Overview

- **FLAC Cover Extraction:** Extracts cover images embedded in FLAC files and saves them as JPEGs.
- **MP3 Album Cover Processing:** Retrieves album cover information from MP3 files and processes them.
- **Standardized Cover Images:** Ensures cover images are in a standardized format (e.g., baseline JPEG, 200x200 pixels).
- **Selectable Preferred Cover** If there are more is more than one image in an album folder, the user can choose the preferred one!

## Prerequisites

- Python 3.x
- FFmpeg installed and added to the system PATH
- Required Python packages: `Pillow`, `eyed3`, `mutagen`

## Installation

```bash
pip install Pillow eyed3 mutagen
```
Install FFmpeg. You can download it from the official [FFmpeg website](https://www.ffmpeg.org/). Make sure it is set in PATH.

```bash
git clone https://github.com/SupItsZaire/rockbox-cover-art-fixer.git
```
```bash
cd rockbox-cover-art-fixer
```
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
- script might break as i have had no one test this yet aside from me :D
