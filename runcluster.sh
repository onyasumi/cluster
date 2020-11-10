#!/bin/sh

echo "Checking Dependencies"

brew --version | grep "Homebrew" || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
python3 --version | grep "Python" || brew install python3
pip3 list | grep "ExifRead" || pip3 install exifread

python3 fixmodtime.py