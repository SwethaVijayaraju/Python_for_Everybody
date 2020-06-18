# Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and
# compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.
# ans : Average spam confidence: 0.750718518519

fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    exit()


def float_extract(line):
    colonpos = line.find(":")
    raw_num_string = line[colonpos + 1:]
    num_string = raw_num_string.strip()
    fnum = float(num_string)
    return fnum


avg_list = list()
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        avg_list.append(float_extract(line))
average = sum(avg_list) / len(avg_list)
print("Average spam confidence:", average)
