#!./env/bin/python3.5
from noaa_sdk import noaa
import re
import csv
import sys
cnt = 1 
header = "elevation[meters], WeatherDataValidUntil, temperature[°F], temperatureTrend, windDirection, windSpeed, shortForecast\n" 
outString = ''
parameters = csv.reader(open('mainData.csv', 'r')) #get long and lat parameters from mainData file
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
        #unit = elevationData.get('unitCode') #formats unit string for elevation 
        #elevation = str(elevation) #+ str(unit) #ommited since all units are meter and easy to express
        #elevation = elevation.replace('unit:', '')
        temp = todayWeather[0].get('temperature')
        time = todayWeather[0].get('endTime')
        tempTrend = todayWeather[0].get('temperatureTrend')
        windDir = todayWeather[0].get('windDirection')
        windSpeed = todayWeather[0].get('windSpeed')
        shortForcast = todayWeather[0].get('shortForecast') 
        outString += str(elevation) + ', ' + str(time) + ', ' + str(temp) + ', ' + str(tempTrend) + ', ' + str(windDir) + ', ' + str(windSpeed) + ', ' + str(shortForcast) + '\n'
        cnt += 1
    except KeyboardInterrupt:
        raise   #this exception allow for ctrl^c to be pressed and program will end
    except: # ignore error that may occor when fethching data from noaa but report them to console
        print('error:', sys.exc_info()[0])
        pass

outString = header + outString 
with open('weatherData.csv', 'w') as f: #write to json file to operate on
    f.write(str(outString))
    f.close()

