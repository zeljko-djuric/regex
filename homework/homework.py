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

for f in os.listdir(homedir):
    stud_dir = os.path.join(homedir, f)
    m = re_dir.match(f)
    if os.path.isdir(stud_dir) and m is not None and f in students:
        student_id = m.group()
        for sf in os.listdir(stud_dir):
            task = os.path.join(stud_dir, sf)
            m = re_file.match(sf)
            if(os.path.isfile(task)) and m is not None:
                task_t = int(m.group(1))
                tasks[(student_id, task_t)] = m.group(2)
                if(task_t > max_num_task):
                    max_num_task = task_t

for student_id, name in students.items():
    print("\nName:" + name)
    for i in range(1, max_num_task):
        if(student_id, i) in tasks:
            print("\t" + str(i) + ". " + tasks[(student_id,i)])
        else:
            print("\t"+ str(i) + ". -")