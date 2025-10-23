# Install PySpark (if using Colab or Jupyter)
# !pip install pyspark

from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

# Create SparkSession
spark = SparkSession.builder.appName('recommendation').getOrCreate()

# Load ratings data
data = spark.read.csv('ratings.csv', inferSchema=True, header=True)

# Preview data
data.head()
data.printSchema()
data.describe().show()

# Split data into train and test sets (80/20)
(train_data, test_data) = data.randomSplit([0.8, 0.2], seed=42)

# Create ALS model
als = ALS(maxIter=15, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating")
model = als.fit(train_data)

# Make predictions on test data
predictions = model.transform(test_data)
predictions.show()

# Evaluate model performance using RMSE
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

# Generate recommendations for a single user (userId=3)
single_user = test_data.filter(test_data['userId']==3).select(['movieId','userId'])
single_user.show()

recommendations = model.transform(single_user)
recommendations.orderBy('prediction', ascending=False).show()
