#!../env/bin/python3.7
import csv
outString = ""
reader1 = csv.reader(open('mainData.csv', 'r')) #acess csv file
rank = 0 # used as counter since know 314 TOP US Cities previous wikitable parse
row1 = next(reader1)[1] #cycle to next row=0, col=1
row1 = next(reader1)[1] # row=1, col=1
row1 = row1[:3] # get first three character of row=1, col=1 of mainData to compare for filtering
row1 = row1.replace(' ', '') # remove excess space from string to compare
reader2 = csv.reader(open('urlData.csv', 'r')) #access the second file with url data
row2 = next(reader2)[0].replace('https://en.wikipedia.org/wiki/', '') #row=0, col=0 note only 0 collum in this file and removes excess hyperlink to use string to compare

with open('mainData.csv', 'r') as f:
    mainData = f.readline() #read 1st line in mainData.cvs
    #mainData = '{}'.format(mainData.strip()) #reads and formats first line into string from mainData csv file
    mainData = f.readline() #read 2nd line
    mainData = '{}'.format(mainData.strip()) # formats 2nd line into string

    with open('urlData.csv', 'r') as g: #to begin parse
        urlData = g.readline() #read 1st line in urlData.csv
        #urlData = '{}'.format(urlData.strip())
        urlData = g.readline() #read 2nd line in urlData.csv, start from here since 1st line is header info
        urlData = '{}'.format(urlData.strip()) #format 2nd line to string
        while (rank <= 314): #only loop 314 time eq to number of Top US Cities 
            #print(rank)
            #print(row1 + ", " + row2)
            row2 = next(reader2)[0].replace('https://en.wikipedia.org/wiki/', '') #1st loop row=1,col[0] and will iterate
            row2 = row2[:2] #get first 2 charcters to use to compare and filer 
            #print(outString)
            if row1 == row2: # compare string to combine city with respective url wiki address
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
            else: 
                urlData = g.readline() #if nothing found iterated bloated urlData file that includes city + state links
                urlData = '{}'.format(urlData.strip()) #format url data into string to put into main file if pass compare statement
                #print (urlData[:3])
                #row1 = row1 #col = 

f = open("testData.csv", 'w')
f.write(str(outString))
f.close()
    
