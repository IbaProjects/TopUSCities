#!./env/bin/python3.5
import re
outString = "Rank, City, State, 2018 estimate, 2010 Census,Change[%], 2016 land area[sq mi], 2016 land area[km*km], 2016 population density[/sq mi], 2016 population density[km*km], location,\n" #1st row list each title for each collumn of data set
with open("testData.csv") as f:
    data = f.readline()
    data = data.replace(u'\ufeff', '') # removes BOM
    data = re.sub(r'\[.\]', '', data) # uses regex to remove footnotes from html
    data = data.split('/', 1)[0] # split after / for coordinates
    n = 1
    cnt = 0
    while data:
        outString += '{}'.format(data.strip())
        outString += ", "
        data = f.readline()
        data = data.replace(u'\ufeff', '')
        data = data.replace('sq mi', '')
        data = data.replace('km2', '')
        data = data.replace('/', ',')
        data = data.replace(';', '')
        #data = data.replace(';
        data = re.sub(r'\[.\]', '', data)
        data = data.split('(', 1)[0] 
        cnt += 1
        if(cnt == 11*n):
            outString += "\n"
            n += 1

outString = outString.replace(',,', ',')
f = open("testData.csv", 'w')
f.write(str(outString))
f.close()
