#this program parses each city individual wiki site to retrieve zip code data
import sys
import re
import requests
from bs4 import BeautifulSoup
import csv
#wiki = "https://en.wikipedia.org/wiki/"
header = 'Zip Codes\n'
outString = header 
cnt = 1
with open("./data/urlData.csv", 'r', encoding='utf-8') as f: 
    with open("./data/wikiData.csv", 'r', encoding='utf-8') as g:
        element = csv.reader(g)
        city = next(element)[1] # call to skip header row
        data = f.readline()
        while (cnt <= 314):
            try:
                data = f.readline()
                dataString = '{}'.format(data.strip())
                url = re.findall(r"\D+$", dataString) # use regex \D is anything but a number + matches 1 or more and $matches end of str
                city = next(element)[1]
                url = url[0].replace(', ', '') #format url string as usable wiki web address for each city
                website_url = requests.get(url).text # webpage for individual city
                #print(city)
                #print(url)
                soup = BeautifulSoup(website_url, 'lxml')
                My_table = soup.find('table',{'class':'infobox'})
                #website_url = requests.get(urlData).text
                zipCodes = My_table.find('div',{'class':'postal-code'}) #use to retrieve zip codes from html
                #for link in links:
                #outString += city + ", "
                outString += '{}'.format(zipCodes.get_text()).replace('\n', ', ') #use replace to keep in row format
                outString = outString.replace(',', ' ')
                outString += "\n"
                print (outString)
                cnt += 1
                print(cnt) #print for feedback should loop 314 times
        
            except KeyboardInterrupt:
                raise
        
            except:            
                #print('error')
                outString += str(city) + " error: parse didn't find zip codes\n"
                #print('error:', sys.exc_info()[0])
                cnt += 1
                pass

f.close()
outString = re.sub(r'\[\w+\]', '', outString) # removes footnotes boxes to clean csv file
f = open("./data/zipCodes.csv", 'w', encoding='utf-8')
f.write(str(outString))
f.close()
