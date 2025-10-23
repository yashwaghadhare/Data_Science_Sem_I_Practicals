from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col
import numpy as np

# Create Spark session
spark = SparkSession.builder.appName("SimilarMoviesALS").getOrCreate()

# Load ratings and movies data
ratings = spark.read.csv("ratings.dat", sep="::", inferSchema=True)\
    .toDF("userId", "movieId", "rating", "timestamp")
movies = spark.read.csv("movies.dat", sep="::", inferSchema=True)\
    .toDF("movieId", "title", "genres")

# Build ALS model
als = ALS(
    userCol="userId",
    itemCol="movieId",
    ratingCol="rating",
    rank=20,
    maxIter=10,
    regParam=0.1,
    coldStartStrategy="drop"
)
model = als.fit(ratings)

# Extract item (movie) factors
movie_factors = model.itemFactors.withColumn("features_vec", col("features"))

# Collect movie features to driver as numpy arrays
movie_features = movie_factors.collect()
id_to_features = {row.id: np.array(row.features) for row in movie_features}

# Map movieId to movie title
movie_title_map = {row.movieId: row.title for row in movies.collect()}

# Function to calculate cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

# Function to get top N similar movies for a given movieId
def get_similar_movies(movie_id, top_n=10):
    if movie_id not in id_to_features:
        return []
    target_vec = id_to_features[movie_id]
    sims = []
    for mid, vec in id_to_features.items():
        if mid == movie_id:
            continue
        sim = cosine_similarity(target_vec, vec)
        sims.append((mid, sim))
    sims.sort(key=lambda x: x[1], reverse=True)
    top = sims[:top_n]
    results = []
    for mid, sim in top:
        title = movies.filter(movies.movieId == mid).select("title").collect()
        title_str = title[0][0] if title else "Unknown"
        results.append((mid, title_str, sim))
    return results

# Example: find top 10 movies similar to movie ID 1193
example_movie_id = 1193
print(f"\nTop 10 movies similar to MovieID {example_movie_id}:\n")
similar_movies = get_similar_movies(example_movie_id, top_n=10)
for mid, title, sim in similar_movies:
    print(f"{title} (id={mid}) — similarity={sim:.4f}")

# Stop Spark session
spark.stop()
