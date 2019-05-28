# this program append two csv files in respective order i.e. FILE_1, FILE_2
# this program also assumed both csv file have mathching row by col 
#define passed arguments from command line
#FILE_1 = sys.argv[1] #first csv file passed to program via command line 
#FILE_2 = sys.argv[2] #second csv file passed 

def append(FILE_1, FILE_2, FILE_NAME = 'combinedData.csv'): #usable function to append two csv file types
    import csv
    outString = '' #used to construct string into formated csv file type
    with open(FILE_1, 'r', encoding='utf-8') as f: 
        with open(FILE_2,  'r', encoding='utf-8') as g:
            reader1 = csv.reader(f) #set reader1 equal to first line of FILE_1 csv file argument passed
            reader2 = csv.reader(g) #set reader2 equal to first line of FILE_2
            r1 = f.readline().replace('\n', '') # remove new line at end of string
            r2 = g.readline().replace('\n', '') # remove new line ad end of string from variable
            while r1: #run while each file line is read until end of file is reached
                outString += str(r1) + ', ' + str(r2) + '\n' # append file 2 to file 1 and add new line at end of formated string
                r1 = f.readline().replace('\n', '') #read next line in file 1 
                r2 = g.readline().replace('\n', '') #read next line in file 2 befor looping again
    #print(outString)
    f.close
    g.close
    h = open(FILE_NAME,'w', encoding='utf-8') #save csv formatted string to newCSV.csv file 
    h.write(str(outString))
    h.close

def main():
    import sys
    FILE_1 = sys.argv[1] #first csv file passed to program via command line 
    FILE_2 = sys.argv[2] #second csv file passed 
    append(FILE_1, FILE_2, FILE_NAME = 'combinedData.csv')

if __name__ == "__main__": main()
