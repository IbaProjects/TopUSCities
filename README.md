# Top US Cities Scrapper
This scrapper collects data on US Top Cites from wikipedia and formats into CSV file type. The program parses wiki page on Top US Cities and writes table info  into .csv file. Each city website link is then parsed to collect zip code information. Optionally, there is python script that uses noaa_sdk to parse city weather data forecast and can be appended to the data set.

## Installation


```bash
git clone https://github.com/IbaProjects/TopUSCities.git
cd TopUSCities
pip install -r requirements.txt
```

## Usage
Go to 'scraper' directory and run python command to generate wikiDataWithZipCodes.csv file in /scraper/data directory. Program parses US Top Cities wikipedia data table then parse each individual city website to collect zip codes.
```bash
cd scraper
python scraper.py
```
NOTE: Terminal will print zip codes as feedback until scraper finishes.

#### Obtain Optional Data
To collect data provide by noaa run the following command. The collection of this data using noaa_sdk is slow and takes about 20 minutes to finish running. The output of this program is file titled "weatherData.csv" Again, starting from the scraper directory:

```bash
python getWeatherData.py
```  
NOTE: Once program start, terminal will print 3 different number as feedback its working(i.e. loop count number, coordinates, and elevation)Be aware the 'getWeatherData.py' take 20+ minutes to run but gathers a good bulk of weather forecast information about each city such as elevation, temperature, datailed forcast, etc. Use appendCSV.py to attach this data set to existing one by performing appendCSV.py operation.
#### To append File_2.csv to FILE_1.csv
This little piece of python code make it easy to combine two .csv data files.

```bash
python appendCSV.py 'FILE_1.csv' 'FILE_2.csv'
```
This allows to easily combine weatherData.csv to mainDataWithZipCodes.csv by running the command from scraper directory:
```bash
python appendCSV.py data/wikiDataWithZipCodes.csv data/weatherData.csv
```

NOTE: both .csv files (i.e. FILE_1.csv and FILE_2.csv) must have the same number of rows to produce a clean .csv data file. Running command will generate combinedData.csv file in current working directory.  
