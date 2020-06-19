# Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("Fine cannot be opened")
    exit()

hours = list()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        hours.append(time[0])

count = dict()
for hour in hours:
    count[hour] = count.get(hour, 0) + 1

sort_lst = sorted(count.items())
for hr, ct in sort_lst:
    print(hr, ct)
