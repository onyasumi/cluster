import os
import time
import exifread

def fixmodtime(indir):

    print("Setting mod dates")

    for i in os.listdir(indir):
        infile = indir + "/" + i
        # Handles subfolders
        if os.path.isfile(infile) == False:
            fixmodtime(infile)
        # Ignores non-image files
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
            print("READ ERROR on file: " + i + ": Cannot read EXIF - File is or does not contain date information")
        
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
