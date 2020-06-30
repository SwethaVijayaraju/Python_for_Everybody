import re

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    exit()
for line in fhand:
    line = line.strip()
    if re.search("File: ", line):
        print(line)
