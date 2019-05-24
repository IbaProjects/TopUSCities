#!./env/bin/python3.5
import re
outString = "\""
with open("testData.csv") as f:
    data = f.readline()
    data = data.replace(u'\ufeff', '') # removes BOM
    data = re.sub(r'\[.\]', '', data) # uses regex to remove footnotes from html
    data = data.split('/', 1)[0] # split after / for coordinates
    n = 1
    cnt = 0
    while data:
        outString += '{}'.format(data.strip())
        outString += "\", \""
        data = f.readline()
        data = data.replace(u'\ufeff', '')
        data = re.sub(r'\[.\]', '', data)
        data = data.split('/', 1)[0] 
        cnt += 1
        if(cnt == 11*n):
            outString += "\n"
            n += 1

outString = outString.replace('\"\n', '\n\"') #fix csv filebefor saving
f = open("testData.csv", 'w')
f.write(str(outString))
f.close()
