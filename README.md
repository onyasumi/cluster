# python-scripts

Python scripts which I created for my own use

## Backstory

Once upon a time, I accidentally wiped a hard drive with over 100GB of pictures on it. Thankfully, I was able to recover my photos, but the original folder structure where they were sorted by date was lost as well as most metadata and the original names of the files.

However, the EXIF data was still there.

Too lazy to re-sort them myself, I leveraged python to sort them for me.

### fixmodtimefromexif.py
For each photo in a given folder, this script reads the date of creation from the EXIF data, and uses it to the metadata to the proper the creation and modification dates. This script is not recursive.

### orgpicsbydate.py
Organizes each photo in a given folder into a folders based on the date of modification [Year/month+day]. Run fixmodtimefromexif.py before running this. This script is not recursive.

### rentoshuttercount.py
This script solves the issue of the files not retaining their original names. It uses the EXIF data of each photo to set the name of the file to the shutter count of the camera (i.e. DSC_3435.NEF, where 3435 is the shutter count). This effectively allows for the files to be sorted based on their order taken. This script is not recursive.

### rmduplicate.py
Removes duplicate files in a given folder by checking SHA1 checksums using a python set. This script is not recursive.
