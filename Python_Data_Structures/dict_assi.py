# Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines
# as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened")
    exit()

mail_list = list()
mail_dict = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        mail_list.append(words[1])
for mail_id in mail_list:
    mail_dict[mail_id] = mail_dict.get(mail_id, 0) + 1

reg_sender = None
sender_count = None
for key, value in mail_dict.items():
    if (sender_count is None) or (sender_count < value):
        sender_count = value
        reg_sender = key
print(reg_sender, sender_count)
