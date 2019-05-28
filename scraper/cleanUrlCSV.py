header = "wikipedia url\n"
testString = ""
outString = header 
with open("./data/urlData.csv", 'r', encoding='utf-8') as f:
    data = f.readline()
    while data:
        testString = '{}'.format(data.strip())
        result = testString.startswith('/wiki/')
        if result == True:
            outString += "https://en.wikipedia.org"
            outString += testString
            outString += "\n"
            data = f.readline()
            testString = ""
        else: 
            testString = ""
            data = f.readline()

f = open("./data/urlData.csv", 'w', encoding='utf-8')
f.write(str(outString))
f.close()
