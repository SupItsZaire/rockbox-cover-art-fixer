# rockbox-cover-art-fixer
A collection of python scripts, to help with Rockbox cover art conversion 
## WINDOWS ONLY AT THE MOMENT

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
Install FFmpeg. You can download it from the official FFmpeg website.

git clone https://github.com/your-username/your-repository.git
cd your-repository

## Usage

Run the script with the command:
```bash
python processandextract.py
```
Select the root directory containing your music folders using the file dialog.

The script will process the folders, extract cover art, and organize the music files.
