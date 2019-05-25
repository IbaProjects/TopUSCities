#!./env/bin/python3.5
header = "wikipedia url,\n"
testString = ""
outString = header 
with open("testData.csv") as f:
    data = f.readline()
    while data:
        testString = '{}'.format(data.strip())
        result = testString.startswith('/wiki/')
        if result == True:
            outString += "https://en.wikipedia.org"
            outString += testString
            outString += ", "
            outString += "\n"
            data = f.readline()
            testString = ""
        else: 
            testString = ""
            data = f.readline()

f = open("testData.csv", 'w')
f.write(str(outString))
f.close()
