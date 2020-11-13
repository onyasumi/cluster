import os
from fixmodtime import fixmodtime
from orgbydate import orgbydate
from renshutter import renshutter
from rmduplicate import rmduplicate

def getpath(mode):
    if(mode):
        print("Please provide a source directory")
    else:
        print("Please provide a destination directory")
    dir = input()
    if(os.name == 'posix'):     # Directory name processing for POSIX systems
        # Gets rid of extra whitespaces
        for i in range(len(dir)):
            if(dir[i] == ' ' and  dir[i-1] != "\\"):
                dir = dir[:i] + dir [i+1:]
        # Gets rid of backslashes for POSIX systems
        dir = dir.replace("\\", "")
    elif(os.name == 'nt'):      # Directory name processing for Windows systems
        True


print("Hello! This is Cluster, a collection of Python 3 scripts that organizes photos using EXIF data")
indir = getpath(True)
outdir = getpath(False)

rmduplicate(indir, set())
fixmodtime(indir)
renshutter(indir)
orgbydate(indir, outdir)