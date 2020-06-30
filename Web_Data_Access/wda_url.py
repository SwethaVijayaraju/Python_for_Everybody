import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_673917.html')
# print(fhand.status)
# print(fhand.read().decode())
for line in fhand:
    print(line.decode().strip())
    # print(type(line))
# print(fhand.info())
# print(type(fhand.info()))
