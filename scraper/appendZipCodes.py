#!./env/bin/python3.7
import csv
outString = ""
reader1 = csv.reader(open('./data/wikiData.csv', 'r')) #acess csv file
rank = 0 # used as counter since know 314 TOP US Cities previous wikitable parse
reader2 = csv.reader(open('./data/zipCodes.csv', 'r')) #access the second file with url data

with open('./data/wikiData.csv', 'r') as f:
    mainData = f.readline() #read 1st line in mainData.cvs
    #mainData = '{}'.format(mainData.strip()) #reads and formats first line into string from mainData csv file
    mainData = '{}'.format(mainData.strip()) # formats 2nd line into string

    with open('./data/zipCodes.csv', 'r') as g: #to begin parse
        urlData = g.readline() #read 1st line in urlData.csv
        #urlData = '{}'.format(urlData.strip())
        urlData = '{}'.format(urlData.strip()) #format 2nd line to string
        while (rank <= 314): #only loop 314 time eq to number of Top US Cities 
            #print(rank)
            #print(row1 + ", " + row2)
            #print(outString)
                rank += 1 #iterate 
                outString += mainData + ', ' + urlData #appends url wiki address to mainData csv file
                mainData = f.readline() #reads 3rd line initialy then iterates
                mainData = '{}'.format(mainData.strip())
                urlData = g.readline() #reads 3rd line or url data file then iterates
                urlData = '{}'.format(urlData.strip())
                outString += '\n'# add new line 
                if rank != 314: #exit loop if false
                    row1 = next(reader1)[1] #row=2, col=1 on initial for mainData file then iterates
                    row1 = row1[:3] #get first 3 characters to compare next row inexed string
                    row1 = row1.replace(' ', '') #remove whitespace
                else: break
                #print(outString) # used for testing script

f.close()
g.close()
f = open("./data/wikiDataWithZipCodes.csv", 'w')
f.write(str(outString))
f.close()
    
