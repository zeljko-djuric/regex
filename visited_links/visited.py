import sys
import re


def visit_directory(dir):
    visited_directories.append(dir)
    try:
        with open(dat, "r") as f:
            data = f.read()
    except IOError:
        sys.exit("File open failed")