# Cluster

Python3 program that ingests photos an SD card (or any other media) to an output directory and sorts them by date taken in a `year/month+day` structure

## How to Use
Install `python3` and `python3-virtualenv`

Clone and cd into the repository and

    ./run.sh

The config file can be found at `settings.yml`

## Other Info

### fixmodtime.py
Sets the proper creation and modification dates for each photo from EXIF data

### orgbydate.py
Organizes each photo in a given folder into a folders based on the date of modification [Year/month+day]

### renshutter.py
Renames each photo to a given prefix and its shutter count (i.e. DSC_3435.NEF, where 3435 is the shutter count).

### rmduplicate.py
Detects and removes duplicate files in a folder using SHA1 checksums.
