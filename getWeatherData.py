#!./env/bin/python3.5
from noaa_sdk import noaa
import re
import csv
import sys
cnt = 1 
header = "elevation[meters], windDirection, temperature[°F], isDaytime, detailedForecast, shortForecast, windSpeed, startTime, number, endTime, name, temperatureTrend, " 
outString = ''
parameters = csv.reader(open('mainData.csv', 'r')) #get long and lat parameters from mainData filewindDir
parameter = next(parameters)[12] #row=0, col=12, note this is the header row

while(cnt<=314):
    try:
        parameter = next(parameters)[12] #row=1, col=12, data that needs to be separated into long and lat    
        longitude = re.search(r'\d+\.\d+', str(parameter)) #search for longitude regular expression for parsing
        longitude = longitude.group() #extract from regex match object 
        latitude = re.search(r'-\d+\.\d+', str(parameter)) #general expression to get lat info
        latitude = latitude.group()
        n = noaa.NOAA()
        print(cnt)
        print(longitude + ', ' + latitude)
        weatherData = n.points_forecast(longitude, latitude, hourly=False) #gets data string
        data = weatherData.pop('properties') #access the key of interest from dict object
        todayWeather = data.pop('periods') #creates list from keys 
        elevationData = data.pop('elevation')
        elevation = elevationData.get('value')
        print(elevation)
        outString += str(elevation) + ', '
        #unit = elevationData.get('unitCode') #formats unit string for elevation 
        #elevation = str(elevation) #+ str(unit) #ommited since all units are meter and easy to express
        #elevation = elevation.replace('unit:', '')
        for i in range(0, 13):
            windDir = todayWeather[i].get('windDirection').replace(',', '-')
            temp = todayWeather[i].get('temperature')
            isDaytime = todayWeather[i].get('isDaytime')
            detailedForecast = todayWeather[i].get('detailedForecast').replace(',', '') #ommit b/c has commas in them
            shortForecast = todayWeather[i].get('shortForecast').replace(',', '')
            windSpeed = todayWeather[i].get('windSpeed').replace(',', '')
            startTime = todayWeather[i].get('startTime')
            number = todayWeather[i].get('number')
            endTime = todayWeather[i].get('endTime')
            name = todayWeather[i].get('name').replace(',', '')
            tempTrend = todayWeather[i].get('temperatureTrend')
            #print(i) #use for testing
            if i != 12:
                outString += str(windDir) + ', ' + str(temp) + ', ' + str(isDaytime) + ', ' + str(detailedForecast) + ', ' + str(shortForecast) + ', ' + str(windSpeed) + ', ' + str(startTime) + ', ' + str(number) + ', ' + str(endTime) + ', ' + str(name) + ', ' + str(tempTrend) + ', ' #appending data in for loop until last line which need to add new line at end of data str
            else: outString += str(windDir) + ', ' + str(temp) + ', ' + str(isDaytime) + ', ' + str(detailedForecast) + ', ' + str(shortForecast) + ', ' + str(windSpeed) + ', ' + str(startTime) + ', ' + str(number) + ', ' + str(endTime) + ', ' + str(name) + ', ' + str(tempTrend) + '\n' #last time in for loop add new line to data string
        cnt += 1
    except KeyboardInterrupt:
        raise   #this exception allow for ctrl^c to be pressed and program will end
    except: # ignore error that may occor when fethching data from noaa but report them to console
        cnt += 1
        print('error:', sys.exc_info()[0])
        pass
h = "windDirection, temperature[°F], isDaytime, detailedForecast, shortForecast, windSpeed, startTime, number, endTime, name, temperatureTrend" # use to attach 13 extra header info for weather of different times of day
outString = header + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + ', ' + h + '\n' + outString #long line due to 12 titles 
with open('weatherData.csv', 'w') as f: #write to json file to operate on
    f.write(str(outString))
    f.close()

