import sys
import re


def visit_directory(dir):
    visited_directories.append(dir)
    try:
        with open(dat, "r") as f:
            data = f.read()
    except IOError:
        sys.exit("File open failed")


regex = re.compile(r'<a\s+href\s*=\s*"(.*?)">.*?</a>',re.I | re.S)

for m in regex.finditer(data):
    url = m.group(1)
    if url not in visited_directories:
        visit_directory(url)

if len(sys.argv) > 1:
    home = sys.argv[1]
else:
    home = "index.html"

