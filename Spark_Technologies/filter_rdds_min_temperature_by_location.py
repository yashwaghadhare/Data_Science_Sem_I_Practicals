from pyspark import SparkConf, SparkContext

# Create Spark context
sc = SparkContext("local", "MinMaxTemperatures")

# Function to parse CSV line
def parseLine(line):
    fields = line.split(',')
    stationID = fields[0]
    entryType = fields[2]
    # Convert temperature to Fahrenheit
    tempF = float(fields[3]) * 0.1 * 9/5 + 32
    return (stationID, entryType, tempF)

# Read and parse CSV
lines = sc.textFile("1800.csv")
parsed = lines.map(parseLine)

# Function to compute min or max temperature
def computeTemp(entryType, func):
    temps = parsed.filter(lambda x: x[1] == entryType)\
                  .map(lambda x: (x[0], x[2]))\
                  .reduceByKey(func)
    return temps.collect()

# Minimum temperatures
for station, temp in computeTemp("TMIN", min):
    print(f"{station}\t{temp:.2f}F")

# Maximum temperatures
for station, temp in computeTemp("TMAX", max):
    print(f"{station}\t{temp:.2f}F")
