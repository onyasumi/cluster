# Cluster

Python3 program that ingests photos from your SD card (or any other media) to your server or NAS (or any other destination directory) and sorts them by date taken in a `year/month+day` structure

## How to Use
Install `python3`

Clone and cd into the repository and run

    pip3 install -r requirements.txt

Then

    python3 runcluster.py

For a fully automated ingestion process, the process can be preconfigured. The configuration can be found at `settings.yml`

## Other Info

### fixmodtime.py
Sets the proper creation and modification dates for each photo from EXIF data

### orgbydate.py
Organizes each photo in a given folder into a folders based on the date of modification [Year/month+day]

### renshutter.py
Renames each photo to a given prefix and its shutter count (i.e. DSC_3435.NEF, where 3435 is the shutter count).

### rmduplicate.py
Detects and removes duplicate files in a folder using SHA1 checksums.
