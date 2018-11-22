import sys
import re
import os

if len(sys.argv) != 2 or re.match(r'^.+\.html$',sys.argv[1]) is None:
    sys.exit("usage: python3 exam.py filepath")

try:
    with open(sys.argv[1],"r") as f:
        data = f.read()
except IOError:
    sys.exit("File open failed")

