#this program cleans the parsed data collected by readWikiToWriteCSV.py program
import re
header = "Rank, City, State, 2018 estimate, 2010 Census,Change[%], 2016 land area[sq mi], 2016 land area[km*km], 2016 population density[/sq mi], 2016 population density[km*km], coordinates[lat° \' \"N long° \' \"W], coordinates[lat°N long°W], coordinates[lat long]\n" #1st row list each title for each collumn of data set
outString = header
with open("./data/wikiData.csv", 'r', encoding='utf-8') as f:
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
outString = outString.replace(' , ', ', ')
outString = outString.replace('\n,', '')
outString = outString.replace(', \n', '\n')
outString = outString.rstrip(', ')
f = open("./data/wikiData.csv", 'w', encoding='utf-8')
f.write(str(outString))
f.close()
