python readWikiToWriteCSVrev1.py #first get wiki data info
python cleanCSVrev1.py #clean info and format info csv file type
python getZipCodes.py #use collect url links get zip codes for each city
python appendCSV.py wikiData.csv zipCodeData.csv #combine both files to produce final data set
mv newCSV.csv USTOPCITYDATA.csv #rename final dataset file
