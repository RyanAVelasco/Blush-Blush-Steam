import urllib.request
fhand = urllib.request.urlopen('https://developers.google.com/edu/python/')
for line in fhand:
    word = line.decode().strip()
    for words in word:
