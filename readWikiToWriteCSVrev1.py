#!./env/bin/python3.7
import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population').text # webpage for data table of interest

soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable sortable'}) #Use BeautifulSoup module to find table on  html website_url
#print(My_table)

links = My_table.findAll('td') #use html links to get title info
#data = My_table.findAll('td')
#print(links)

#cities = []

outString = "" #define outString to hold data
# for loop gets City, State data and store information in outString 
for link in links: #for loop through links table information to create data structure
    outString += '{}'.format(link.get_text())
    outString = outString.replace(',', '') # remove commasfrom strings
    outString = outString.replace(' , ', ', ')
    outString += ", " #used to seperate value by comma for file type 
    #outString += "\n"
#print(cities) #alternative method to use
#for states in outString:
    
f = open('wikiData.csv','w') #create csv file to write to 
f.write(str(outString)) #write data of interest to file created.
f.close()

