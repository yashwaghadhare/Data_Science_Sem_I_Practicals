from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
import numpy as np

# Create Spark session
spark = SparkSession.builder.appName("SimilarMoviesALS").getOrCreate()

# Load ratings and movies data
ratings = spark.read.csv("ratings.dat", sep="::", inferSchema=True)\
    .toDF("userId", "movieId", "rating", "timestamp")
movies = spark.read.csv("movies.dat", sep="::", inferSchema=True)\
    .toDF("movieId", "title", "genres")

# Train ALS model
als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating",
          rank=20, maxIter=10, regParam=0.1, coldStartStrategy="drop")
model = als.fit(ratings)

# Collect movie factors as numpy arrays
movie_features = {row.id: np.array(row.features) for row in model.itemFactors.collect()}
movie_titles = {row.movieId: row.title for row in movies.collect()}

# Cosine similarity function
def cosine_sim(v1, v2):
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# Get top N similar movies
def get_similar(movie_id, top_n=10):
    if movie_id not in movie_features:
        return []
    target = movie_features[movie_id]
    sims = [(mid, cosine_sim(target, vec)) for mid, vec in movie_features.items() if mid != movie_id]
    sims.sort(key=lambda x: x[1], reverse=True)
    return [(mid, movie_titles.get(mid, "Unknown"), sim) for mid, sim in sims[:top_n]]

# Example: top 10 movies similar to movie ID 1193
for mid, title, sim in get_similar(1193):
    print(f"{title} (id={mid}) — similarity={sim:.4f}")

# Stop Spark session
spark.stop()
