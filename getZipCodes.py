#!./env/bin/python3.5
#this program parses each city individual wiki site to retrieve zip code data
import re
import requests
from bs4 import BeautifulSoup
import csv
wiki = "https://en.wikipedia.org/wiki/"
element = csv.reader(open("mainData.csv", 'r'))
city = next(element)[1] # call to skip header row
header = 'Zip Codes\n'
outString = header 
cnt = 1
with open("mainDataWithURL.csv") as f:
    data = True 
    while cnt <= 314:
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

            links = My_table.find('div',{'class':'postal-code'})
            #for link in links:
            #outString += city + ", "
            outString += '{}'.format(links.get_text()).replace('\n', ', ') #use replace to keep in row format
            outString = outString.replace(',', ' ')
            outString += "\n"
            print (outString)
            cnt += 1
            print(cnt) #print for feedback should loop 314 times
        except:
            #print('error')
            outString += city + " error: parse didn't find zip codes\n"
            cnt +=1
            pass

outString = re.sub(r'\[\w+\]', '', outString) # removes footnotes boxes to clean csv file
f = open("zipCodeData.csv", 'w')
f.write(str(outString))
f.close()
