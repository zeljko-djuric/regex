import sys
import re
import os

homedir = 'homeworks'
students = {}

file_path = os.path.join(homedir, "student_id")
try:
    with open(file_path, "r") as f:
        for line in f.readlines():
            if(line[-1] == '\n'):
                line = line[:-1]
            if re.match(r'm[mnvlri]\d{5},\s*[A-Za-z ]+',line) is not None:
                info = re.split(r',\s*',linija)
                students[info[0]] = info[1]
except IOError:
    sys.exit("File open failed!")

re_dir = re.compile(r'm[mnvlri]\d{5}$')
re_file = re.compile(r'^(\d)\.(java|pas|c|cpp)$')

max_num_task = 0
tasks = {}
