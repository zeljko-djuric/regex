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

pattern = re.compile(r'{(.*?),\.NE\+([a-z]+):[0-9][a-z]}',re.S)

replace = pattern.sub(r'<\2>\1<\2>',data)

try:
    with open(sys.argv[1][:-3]+"xml","w") as fxml:
        fxml.write("<xml>\n")
        fxml.write(replace)
        fxml.write("\n</xml>")
except IOError:
    sys.exit("write() failed")