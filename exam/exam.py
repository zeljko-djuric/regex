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

students = []
points = []

re_data = re.compile(r'<tr>'+
r'\s*<td>\s*(?P<name>[A-Za-z]+( [A-Za-z]+)+)\s*</td>'+
r'\s*<td>\s*(?P<practical>\d|[1-9]\d|100)</td>'+
r'\s*<td>\s*(?P<theory>\d[1-9]\d|100)</td>'+
r'\s*</tr>')

m = re_data.search(data)

while m is not None:
    students.append(m.group('name'))
    all_points = int(m.group('practical')) + int(m.group('theory'))
    points.append(all_points/2)
    m = re_data.search(data,m.end())

