from fixmodtime import fixmodtime
from orgbydate import orgbydate
from renshutter import renshutter
from rmduplicate import rmduplicate

try:
    import exifread
except:
    os.system("pip3 install exif-py")
    import exifread

def getpath(input):
    if(input):
        print("Please provide a source directory")
    else:
        print("Please provide a destination directory")
    indir = input()
    indir = indir.replace("\\", "")

print("Hello! This is Cluster, a collection of Python 3 scripts that organizes photos using EXIF data")
print("Currently, these scripts only support POSIX systems (No Windows). Please do not leave any extra spaces when inputting directories.")
indir = getpath(True)
outdir = getpath(False)

rmduplicate(indir)
fixmodtime(indir)
renshutter(indir)
orgbydate(indir)