from pyspark.sql import SparkSession

# Start Spark session
spark = SparkSession.builder.appName("BroadcastMovies").getOrCreate()
sc = spark.sparkContext

# Load movie names into a dictionary and broadcast
movieNames = {}
with open("movies.dat", encoding="ISO-8859-1") as f:
    for line in f:
        movieId, title = line.strip().split("::")[:2]
        movieNames[int(movieId)] = title
movieNamesBr = sc.broadcast(movieNames)

# Load and parse ratings
ratings = sc.textFile("ratings.dat") \
            .map(lambda l: l.split("::")) \
            .map(lambda f: (int(f[0]), int(f[1]), float(f[2])))

# Add movie names using broadcast variable
ratingsWithNames = ratings.map(lambda x: (x[0], movieNamesBr.value.get(x[1], "Unknown"), x[2]))

# Show first 10 results
for r in ratingsWithNames.take(10):
    print(r)

# Stop Spark session
spark.stop()