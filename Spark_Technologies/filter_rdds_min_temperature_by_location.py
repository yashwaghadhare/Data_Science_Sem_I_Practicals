# !pip install pyspark

from pyspark import SparkConf, SparkContext

# Create Spark configuration and context
conf = SparkConf().setMaster("local").setAppName("MinMaxTemperatures")
sc = SparkContext(conf = conf)

# Function to parse each line of CSV
def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) * 0.1 * (9.0 / 5.0) + 32.0
    return (stationID, entryType, temperature)

# Read CSV file and parse lines
lines = sc.textFile("1800.csv")
parsedLines = lines.map(parseLine)

# Find Minimum Temperatures
minTemps = parsedLines.filter(lambda x: "TMIN" in x[1])
stationTemps = minTemps.map(lambda x: (x[0], x[2]))
minTemps = stationTemps.reduceByKey(lambda x, y: min(x, y))
results = minTemps.collect()
for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))

# Find Maximum Temperatures
parsedLines = lines.map(parseLine)
maxTemps = parsedLines.filter(lambda x: "TMAX" in x[1])
stationTemps = maxTemps.map(lambda x: (x[0], x[2]))
maxTemps = stationTemps.reduceByKey(lambda x, y: max(x, y))
results = maxTemps.collect()
for result in results:
    print(result[0] + "\t{:.2f}F".format(result[1]))
