# Cluster

A collection of Python 3 scripts that organizes photos using EXIF data

## How to Use
### Mac OS/Linux: run `runcluster.sh`
### Windows: Install Python 3, install the package`exifread` (`pip3 install exifread`) and run `organizephotos.py` (`python3 ~/scripts/organizephotos.py`)

## Backstory
I accidentally wiped a hard drive with over 100GB of pictures on it. After running file recovery, the original folder structure, most metadata, and the original filenames were lost.

However, the EXIF data was recovered.

Too lazy to re-sort the photos myself, I wrote some python scripts to sort them for me.

### fixmodtime.py
For each photo in a given folder, this script reads the date of creation from the EXIF data, and uses it to the metadata to the proper the creation and modification dates.

### orgbydate.py
Organizes each photo in a given folder into a folders based on the date of modification [Year/month+day]. Run fixmodtimefromexif.py before running this.

### renshutter.py
This script solves the issue of the files not retaining their original names. It uses the EXIF data of each photo to set the name of the file to the shutter count of the camera (i.e. DSC_3435.NEF, where 3435 is the shutter count). This effectively allows for the files to be sorted based on their order taken.

### rmduplicate.py
Removes duplicate files in a given folder by checking SHA1 checksums using a python set.
