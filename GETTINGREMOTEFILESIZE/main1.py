import urllib.request

url = 'https://www.youtube.com/watch?v=W2FANfuYoK0'
usock = urllib.request.urlopen(url)
data = usock.read()
size = data.__len__() # size in bytes
size = size / 1024.0 # in KB (Kilo Bytes)
size = size / 1024.0 # size in MB (Mega Bytes)
size = float(round(size, 3))
print(size, "MB")