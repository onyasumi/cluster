import os
from ruamel.yaml import YAML
from scripts.fixmodtime import fixmodtime
from scripts.orgbydate import orgbydate
from scripts.renshutter import renshutter
from scripts.rmduplicate import rmduplicate

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

# Reads the config file
useconfigfile = False
indir = ""
outdir = ""
prefix = ""

if os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + "/requirements.txt"):
    pass
else:
    configfile = open(os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + "/requirements.txt"), "r")
    confyaml = YAML(typ="safe").load(configfile)
    try:
        useconfigfile = confyaml["useconfig"]
    except:
        pass

    try:
        indir = confyaml["source_directory"]
    except:
        pass

    try:
        outdir = confyaml["output_directory"]
    except:
        pass

    try:
        prefix = confyaml["file_prefix"]
    except:
        pass
    
print("Hello! This is Cluster, a photo ingestion program written in Python 3")

while os.path.isdir(indir) == False:
        indir = getpath(True)

while os.path.isdir(outdir) == False:
        outdir = getpath(False)

while prefix != "":
    print("Please specify a prefix (i.e. \"DSC_\")")
    prefix = input()

rmduplicate(indir, set())
fixmodtime(indir)
renshutter(indir, prefix)
orgbydate(indir, outdir)