import re, sys

if len(sys.argv) != 2:
    sys.exit("usage: python3 converter.py filePath")

if re.match(r'^[\w_-]+\.stn$',sys.argv[1]) is None:
    sys.exit('File extension must be .stn')

try:
    with open(argv[1],"r") as f:
        data = f.read()
except IOError:
    sys.exit('File open failed')

