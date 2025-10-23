from pyspark import SparkConf, SparkContext

# Create Spark configuration and context
conf = SparkConf().setMaster("local").setAppName("TotalTimeSpend")
sc = SparkContext(conf=conf)

# Function to extract (customerID, timeSpent) from CSV line
def extractValue(line):
    fields = line.split(',')
    return (int(fields[0]), int(float(fields[2])))

# Read CSV file
lines = sc.textFile("customer-orders.csv")

# Map to (customerID, timeSpent)
mappedInput = lines.map(extractValue)

# Reduce by key to get total time spent per customer
totalTimeSpend = mappedInput.reduceByKey(lambda x, y: x + y)
results = totalTimeSpend.collect()

# Print results
for result in results:
    print(result)

# Example of using broadcast variable
rdd = sc.parallelize(range(10))
a_big_list = [1, 5]

# Without broadcast
result = rdd.map(lambda x: (x, x in a_big_list)).collect()

# Using broadcast variable for efficiency
a_big_list_br = sc.broadcast(a_big_list)
result = rdd.map(lambda x: (x, x in a_big_list_br.value)).collect()

# Print example
print(result[2])

# Stop SparkContext
sc.stop()
