import os
import time
import exifread

def renshutter(indir, prefix):
    
    for i in os.listdir(indir):
        
        infile = indir + "/" + i
        # Handles subfolders
        if os.path.isfile(infile) == False:
            renshutter(infile)
        # Ignores non-image files
        if ((i.lower().endswith("jpg") == False) and (i.lower().endswith("jpeg") == False) and (i.lower().endswith("tif") == False) and (i.lower().endswith("tiff") == False) and (i.lower().endswith("cr2") == False) and (i.lower().endswith("nef") == False)):
            continue
        
        file = open(infile, "rb")
        try:
            tags = exifread.process_file(file)
            shuttercount = str(tags["MakerNote TotalShutterReleases"])
        except:
            print("READ ERROR on file " + i + ": Cannot read EXIF - File is corrupt or does not contain shutter information")
        try:
            print("Renaming " + i + " to " + prefix + shuttercount + "." + i.split(".")[-1])
            os.rename(infile, indir + "/" + prefix + shuttercount + "." + i.split(".")[-1])
        except:
            print("WRITE ERROR ON " + i + ": Insufficient privileges?")

    print("Done")
