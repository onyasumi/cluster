import os
import time
import shutil
import organizephotos

def orgbydate(indir, outdir):
    
    while os.path.isdir(indir) == False:
        indir = getpath(True)

    while os.path.isdir(outdir) == False:
        outdir = getpath(False)

    print("Moving files")

    for i in os.listdir(indir):
        infile = indir + "/" + i
        # Handles subfolders
        if os.path.isfile(infile) == False:
            orgbydate(infile, outdir)
        # Ignores non-image files
        if ((i.lower().endswith("jpg") == False) and (i.lower().endswith("jpeg") == False) and (i.lower().endswith("cr2") == False) and (i.lower().endswith("nef") == False)):
            continue

        unixtime = int(os.path.getmtime(infile))
        year = time.localtime(unixtime).tm_year
        month = time.localtime(unixtime).tm_mon
        day = time.localtime(unixtime).tm_mday

        monthnames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        
        # Checks if target directory exists
        targetdir = outdir + "/" + str(year) + "/" + monthnames[month-1] + " " + str(day) + "/"
        if os.path.isdir(targetdir) == False:
            print("Creating directory " + targetdir)
            os.makedirs(targetdir)
        
        print("Moving " + i + " to " + targetdir + i)
        shutil.copy2(infile, targetdir + i)

    print("Done")
