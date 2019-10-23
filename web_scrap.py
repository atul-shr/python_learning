import urllib.request
import re

url = "https://www.youtube.com/watch?v=zN8rwVXwRUE"

res = urllib.request.urlopen(url)

html = res.read()

htmlstr = html.decode()

# print(htmlstr)
readdata = re.findall("[.\w]*\ssubscribers",htmlstr)

print(readdata)
