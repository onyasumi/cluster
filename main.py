import os
from ruamel.yaml import YAML
from scripts.fixmodtime import fixmodtime
from scripts.orgbydate import orgbydate
from scripts.renshutter import renshutter
from scripts.rmduplicate import rmduplicate


print(os.path.dirname(os.path.realpath(__file__)) + "/settings.yaml")

# Reads the config file
configfile = open(os.path.dirname(os.path.realpath(__file__)) + "/settings.yaml", "r")
confyaml = YAML(typ="safe").load(configfile)
srcdir = confyaml["source_directory"]
destdir = confyaml["output_directory"]
prefix = confyaml["file_prefix"]

if not os.path.isdir(srcdir):
    raise Exception("Source directory doesn't exist")

if not os.path.isdir(destdir):
    raise Exception("Destination directory doesn't exist")

if prefix != "":
    raise ValueError("Prefix is an empty string. Continuing.")


print("Configuration OK. Continuing")

rmduplicate(srcdir, set())
fixmodtime(srcdir)
renshutter(srcdir, prefix)
orgbydate(srcdir, destdir)
