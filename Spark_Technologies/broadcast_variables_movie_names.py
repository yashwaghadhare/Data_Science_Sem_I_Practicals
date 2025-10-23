from pyspark.sql import SparkSession

# Create SparkSession and SparkContext
spark = SparkSession.builder.appName("BroadcastMovieNames").getOrCreate()
sc = spark.sparkContext

# Function to load movie names into a dictionary
def loadMovieNames():
    movieNames = {}
    with open("movies.dat", encoding="ISO-8859-1") as f:
        for line in f:
            fields = line.strip().split("::")
            if len(fields) >= 2:
                movieId = int(fields[0])
                movieName = fields[1]
                movieNames[movieId] = movieName
    return movieNames

# Load movie names and broadcast to all worker nodes
movieNamesDict = loadMovieNames()
movieNamesBroadcast = sc.broadcast(movieNamesDict)

# Load ratings data
ratings = sc.textFile("ratings.dat")

# Parse ratings into (userID, movieID, rating)
ratingsParsed = ratings.map(lambda l: l.split("::")) \
                       .map(lambda f: (int(f[0]), int(f[1]), float(f[2])))

# Map ratings to include movie names using broadcast variable
ratingsWithNames = ratingsParsed.map(
    lambda x: (x[0], movieNamesBroadcast.value.get(x[1], "Unknown"), x[2])
)

# Show first 10 results
for result in ratingsWithNames.take(10):
    print(result)

# Stop SparkSession
spark.stop()
