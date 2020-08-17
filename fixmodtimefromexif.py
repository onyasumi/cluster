import os
import time
import exifread

print("Welcome! This script bulk resets the date of modification and creation to the date taken for all files inside a folder")
print("Requires exif-py to be installed and a POSIX system to work correctly")

indir = "notADir"
while os.path.isdir(indir) == False:
    print("Input directory not found or invalid. Please input a source directory, without extra whitespaces")
    indir = input()
    indir = indir.replace("\\", "")

print("Setting mod dates")

for i in os.listdir(indir):
    
    infile = indir + "/" + i
    #ignores non-files
    if os.path.isfile(infile) == False:
        continue
    #ignores non-image files
    if ((i.lower().endswith("jpg") == False) and (i.lower().endswith("jpeg") == False) and (i.lower().endswith("tif") == False) and (i.lower().endswith("tiff") == False) and (i.lower().endswith("cr2") == False) and (i.lower().endswith("nef") == False)):
        continue
    
    timetaken = ":"
    file = open(infile, "rb")
    try:
        tags = exifread.process_file(file)
        timetaken = str(tags["Image DateTime"])
        timetaken = timetaken.replace(" ",":")
        timetaken = timetaken.split(":")
        timetaken = [int(x) for x in timetaken]
        timetaken = tuple(timetaken) + (0,0,0)
    except:
        print("READ ERROR on file: " + i + ": Cannot read EXIF - File is probably corrupt OR exif-py not installed")
        print("Please type <pip install exifread> to install exif-py")
    
    try:
        timetaken = time.mktime(timetaken)
    except:
        print(timetaken)
        print("Please type <pip install exifread> to install exif-py")
    
    try:
        print("Setting mod dates on " + infile)
        os.utime(infile, (timetaken, timetaken))
    except:
        print("WRITE ERROR on file " + i + ": Insufficient privileges?")

print("Done")
print("Press ENTER to exit")
input()
