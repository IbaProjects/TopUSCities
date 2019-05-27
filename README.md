# Top US Cities Scrapper
This scrapper collects data on US Top Cites from wikipedia and formats into CSV file type. The program parses wiki page on Top US Cities and writes table info  into .csv file. Each city website link is then parsed to collect zip code information. Optionally, there is python script that uses noaa_sdk to parse city weather data forecast and can be appended to the data set.

## Installation


```bash
pip install requirements.txt
```

## Usage
Entering the following command will generate USTOPCITYDATA.csv file in current directory. Program parses US Top Cities wikipedia data table then parse each individual city website to collect zip codes.
```bash
./runScrapper.py
```

#### Optionally
To collect data provide by noaa run the following command. The collection of this data using noaa_sdk is slow and takes about 20 minutes to finish running. The output of this program is file titled "weatherData.csv"

```bash
./getWeatherData.py
```  
#### To append File_2.csv to FILE_1.csv
This little piece of python code make it easy to combine two .csv data files.

```bash
./appendCSV.py 'FILE_1.csv' 'FILE_2.csv'
```
This allows to easily combine weatherData.csv to USTOPCITYDATA.csv by running the command:
```bash
./appendCSV.py USTOPCITYDATA.csv weatherData.csv
```

NOTE: both .csv files (i.e. FILE_1.csv and FILE_2.csv) must have the same number of rows to produce a clean .csv data file. Running command will generate newCSV.csv file in current directory.  
