import os
import exifread


def renshutter(indir, prefix):
    print("Renaming Files")

    for i in os.listdir(indir):

        infile = indir + "/" + i
        # Handles subfolders
        if os.path.isfile(infile) == False:
            renshutter(infile)
        # Ignores non-image files
        if ((i.lower().endswith("jpg") == False) and (i.lower().endswith("jpeg") == False) and (
                i.lower().endswith("tif") == False) and (i.lower().endswith("tiff") == False) and (
                i.lower().endswith("cr2") == False) and (i.lower().endswith("nef") == False) and (
                i.lower().endswith("arw") == False)):
            continue

        file = open(infile, "rb")
        try:
            tags = exifread.process_file(file)
            shuttercount = str(tags["MakerNote TotalShutterReleases"])
        except Exception as e:
            print("READ ERROR on file " + i + ": Cannot read EXIF - File is corrupt or does not contain shutter information")
            print(e)

        try:
            print("Renaming " + i + " to " + prefix + shuttercount + "." + i.split(".")[-1])
            os.rename(infile, indir + "/" + prefix + shuttercount + "." + i.split(".")[-1])
        except:
            print("WRITE ERROR ON " + i + ": Insufficient privileges?")

    print("Done")
