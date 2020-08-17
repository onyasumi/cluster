import os
import time
import shutil

print("Welcome! This script sorts your NEFs based on their date of last modified")
print("This script assumes a POSIX-compliant system (i.e. MacOS, Linux, etc)")
print("DOES NOT WORK WITH WINDOWS/DOS\n")

indir = "notADir"
while os.path.isdir(indir) == False:
    print("Input directory not found or invalid. Please provide a source directory, without extra whitespaces")
    indir = input()
    indir = indir.replace("\\", "")

outdir = "notADir"
while os.path.isdir(outdir) == False:
    print("Output directory not found or invalid. Please input an output directory. NOTE: A new parent folder will not be created")
    outdir = input()
    outdir = outdir.replace("\\", "")

print("Moving files")

for i in os.listdir(indir):
    infile = indir + "/" + i
    #ignores non-files
    if os.path.isfile(infile) == False:
        continue
    #ignores non-image files
    if ((i.lower().endswith("jpg") == False) and (i.lower().endswith("jpeg") == False) and (i.lower().endswith("cr2") == False) and (i.lower().endswith("nef") == False)):
        continue

    unixtime = int(os.path.getmtime(infile))
    year = time.localtime(unixtime).tm_year
    month = time.localtime(unixtime).tm_mon
    day = time.localtime(unixtime).tm_mday

    monthnames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    #Checks if target directory exists
    targetdir = outdir + "/" + str(year) + "/" + monthnames[month-1] + " " + str(day) + "/"
    if os.path.isdir(targetdir) == False:
        print("Creating directory " + targetdir)
        os.makedirs(targetdir)
    
    print("Moving " + i + " to " + targetdir + i)
    shutil.copy2(infile, targetdir + i)

print("Done")
