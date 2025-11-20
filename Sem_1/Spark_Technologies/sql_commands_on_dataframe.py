from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create SparkSession
spark = SparkSession.builder.config("spark.sql.warehouse.dir","file:///C:/temp").appName("ABCSDND").getOrCreate()

# Function to parse each CSV line into a Row
def mapper(line):
    fields = line.split(',')
    return Row(
        ID=int(fields[0]),
        name=str(fields[1].encode("utf-8")),
        age=int(fields[2]),
        numFriends=int(fields[3])
    )

# Load CSV file
lines = spark.sparkContext.textFile("fakefriends.csv")

# Map lines to Row objects
people = lines.map(mapper)

# Create DataFrame and cache it
schemaPeople = spark.createDataFrame(people).cache()

# Register DataFrame as a temporary SQL view
schemaPeople.createOrReplaceTempView("People")

# Query: Select all teenagers (age 13-19)
queryA = spark.sql("SELECT * FROM People WHERE age >=13 AND age <=19")
for rec in queryA.collect():
    print(rec)

# Group by age, count, and order by age
queryA.groupBy("age").count().orderBy("age").show()

# Stop SparkSession
spark.stop()
