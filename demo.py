import sys
import re

if len(sys.argv) != 2:
    sys.exit("python3 demo.py file_path")

if re.match(r'.+\.txt',sys.argv[1],re.I) is None:
    sys.exit("Extension must be .txt")

ri = re.compile(r'(?i)(\b[A-Za-z]+\b)\s+\1')

try:
    f = open(sys.argv[1],"r")
except IOError:
    sys.exit("File open failed!")

for line in f:
    match = ri.search(line)
    if match is not None:
        print("Matching: %s\t groups: %s"%(match.group(), match.groups()))
        print("Line without matching: " + ri.sub('anything', line))
    
f.close()
