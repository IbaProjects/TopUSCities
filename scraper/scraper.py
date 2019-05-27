#this scraper runs in order of operation to retrieve data from wikipedia
import readWikiToWriteCSVrev1
import cleanCSVrev1 
import getZipCodes 
import appendZipCodes
readWikiToWriteCSVrev1 #first get wiki data info
cleanCSVrev1 #clean info and format info csv file type
getZipCodes #use collect url links get zip codes for each city
appendZipCodes #combine both files to attach zip codes. I wrote this python scrip early on in this assignment but alternatively can use appendCSV.py script. Either way, this works. 
