#!./env/bin/python3.5
# this program append two csv files in respective order i.e. FILE_1, FILE_2
# this program also assumed both csv file have mathching row by col 
import sys
import csv
#define passed arguments from command line
FILE_1 = sys.argv[1] #first csv file passed to program via command line 
FILE_2 = sys.argv[2] #second csv file passed 

outString = ''
with open(FILE_1, 'r') as f:
    with open(FILE_2,  'r') as g:
        reader1 = csv.reader(f)
        reader2 = csv.reader(g)
        r1 = f.readline().replace('\n', '') 
        r2 = g.readline().replace('\n', '')
        while r1: 
            outString += str(r1) + ', ' + str(r2) + '\n'
            r1 = f.readline().replace('\n', '') 
            r2 = g.readline().replace('\n', '')
             

#print(outString)
f.close
g.close
h = open('newCSV.csv','w')
h.write(str(outString))
h.close
