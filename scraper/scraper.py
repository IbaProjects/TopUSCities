#this scraper runs in order of operation to retrieve data from wikipedia
import readWikiToWriteURL 
import cleanUrlCSV 
import readWikiToWriteCSVrev1 #parse wikidata table
import cleanCSVrev1 #clean and format to csv file type
import filterURLData #removes extra url links (i.e. US States links) for url parse in getZipCodes
import getZipCodes
from appendCSV import append #use to combine wikiData.csv and zipCodes.csv

readWikiToWriteURL #get url list to transverse programatically
cleanUrlCSV #clean url file so its easy to parse, can't include url list of cities in csv format becasue all urls have commas in them.
readWikiToWriteCSVrev1 #first get wiki data info
cleanCSVrev1 #clean wikiData info and format info csv file type
filterURLData
getZipCodes #use collected url links to get zip codes from each city website
FILE_1 = './data/wikiData.csv'
FILE_2 = './data/zipCodes.csv'
append(FILE_1, FILE_2, FILE_NAME = './data/wikiDataWithZipCodes.csv') #combine both files to attach zipCodes useing appendCSV.py script I wrote and outputs a new FILE_NAME = /data/wikiDataWithZipCodes.csv 
