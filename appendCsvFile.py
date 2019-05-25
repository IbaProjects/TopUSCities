#!./env/bin/python3.5
import csv
outString = ""
reader1 = csv.reader(open('mainData.csv', 'r'))
rank = 1
row1 = next(reader1)[1]
row1 = next(reader1)[1]
row1 = row1[:3]
row1 = row1.replace(' ', '')
reader2 = csv.reader(open('urlData.csv', 'r'))
row2 = next(reader2)[0].replace('https://en.wikipedia.org/wiki/', '')

with open('mainData.csv', 'r') as f:
    mainData = f.readline()
    mainData = '{}'.format(mainData.strip())
    mainData = f.readline()
    mainData = '{}'.format(mainData.strip())

    with open('urlData.csv', 'r') as g:
        urlData = g.readline()
        urlData = '{}'.format(urlData.strip())
        urlData = g.readline()
        urlData = '{}'.format(urlData.strip())
        while rank <= 314:
            #print(rank)
            #print(row1 + ", " + row2)
            row2 = next(reader2)[0].replace('https://en.wikipedia.org/wiki/', '')
            row2 = row2[:2]
            #print(outString)
            if row1 == row2:
                rank += 1
                outString += mainData + ' ' + urlData
                mainData = f.readline()
                mainData = '{}'.format(mainData.strip())
                urlData = g.readline()
                urlData = '{}'.format(urlData.strip())
                outString += '\n'
                row1 = next(reader1)[1]
                row1 = row1[:3]
                row1 = row1.replace(' ', '')
            #    print(outString)
            else: 
                urlData = g.readline()
                urlData = '{}'.format(urlData.strip())
                #print (urlData[:3])
                row1 = row1

f = open("testData.csv", 'w')
f.write(str(outString))
f.close()
    
