# Top US Cities Scraper
This scraper collects data on US Top Cites from
[Wikipedia] and formats into CSV file type. The program parses wiki page on Top US Cities and writes table info  into .csv file. Each city website link is then parsed to collect zip code information. Optionally, there is python script that uses [noaa_sdk] to parse city weather data forecast and can be appended to the data set.

[Wikipedia]:https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population
## Installation MacOS/Linux/Windows(replace python with py.exe)
[noaa_sdk]: https://github.com/paulokuong/noaa

```bash
git clone https://github.com/IbaProjects/TopUSCities.git
cd TopUSCities/
python -m pip install -r requirements.txt
```

## Usage MacOS/Linux/Windows(replace python with py.exe)
Go to 'scraper' directory and run python command to generate csv file in /scraper/data directory. Program parses US Top Cities wikipedia data table then parse each individual city website to collect zip codes.
```bash
cd scraper/
python scraper.py
```
NOTE: Terminal will print zip codes as feedback until scraper finishes. CSV file generated is in data directory named 'wikiDataWithZipCodes'.

#### Obtain Optional Data
To collect data provide by noaa run the following command. The collection of this data using noaa_sdk is slow and takes about 20 minutes to finish running. The output of this program is file titled "weatherData.csv" Again, starting from the scraper directory:

```bash
python getWeatherData.py
```  
NOTE: Once program start, terminal will print 3 different number as feedback its working(i.e. loop count number, coordinates, and elevation)Be aware the 'getWeatherData.py' take 20+ minutes to run but gathers a good bulk of weather forecast information about each city such as elevation, temperature, datailed forcast, etc. Use appendCSV.py to attach this data set to existing one by performing appendCSV.py operation.

#### To append File_2.csv to FILE_1.csv
This little piece of python code make it easy to combine two .csv data files.

```bash
python appendCSV.py 'FILE_1.csv' 'FILE_2.csv' 'FILE_NAME=optional'
```
This allows to easily combine weatherData.csv to mainDataWithZipCodes.csv by running the command from scraper directory:
```bash
python appendCSV.py data/wikiDataWithZipCodes.csv data/weatherData.csv
```

NOTE: both .csv files (i.e. FILE_1.csv and FILE_2.csv) must have the same number of rows to produce a clean .csv data file. Running command will generate combinedData.csv file in current working directory.  

#### Directory of data files
```bash
cd data/
```
Data files are located in the data folder. By default COPY of data files scraper produces are included. If program succeeds in running, new filenames will appear in data folder without the 'COPY' text appended.
