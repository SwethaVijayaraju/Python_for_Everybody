# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
import re

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    quit()
numlist = list()
for line in fhand:
    line = line.rstrip()
    if re.search('[0-9.]+', line):
        raw_data = re.findall('[0-9.]+', line)
        for str_num in raw_data:
            try:
                num = float(str_num)
            except:
                continue
            numlist.append(num)
print(sum(numlist))
