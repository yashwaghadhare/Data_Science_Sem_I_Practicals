from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, when, count, trim, lower
from pyspark.ml.feature import Imputer

# Create Spark session
spark = SparkSession.builder.appName("MissingDataHandling").getOrCreate()

# Sample data with missing values
data = [
    (1, "Alice", 25, None), (2, "Bob", None, 4000),
    (3, None, 30, 5000), (4, "David", 45, None),
    (5, "Eve", None, None), (6, "Alice", 25, None)
]
columns = ["id", "name", "age", "salary"]
df = spark.createDataFrame(data, columns)

# Show DataFrame
df.show()

# Detect missing values per column
df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show()

# Drop rows with any nulls
df.na.drop(how="any").show()

# Drop rows with all nulls
df.na.drop(how="all").show()

# Drop rows where specific columns are null
df.na.drop(subset=["age", "salary"]).show()

# Fill missing values with constants
df_fill = df.na.fill({"name": "Unknown", "age": 0, "salary": 0})
df_fill.show()

# Impute missing numeric values (mean or median)
imputer = Imputer(inputCols=["age", "salary"], outputCols=["age_imputed", "salary_imputed"])\
    .setStrategy("mean")  # or "median"
df_imputed = imputer.fit(df).transform(df)
df_imputed.show()

# Replace specific values
df_replace = df.replace(["Alice"], ["Alicia"], "name")
df_replace.show()

# Remove duplicate rows
df_dedup = df.dropDuplicates()
df_dedup.show()

# Clean text columns: lowercase and trim spaces
df_clean = df.withColumn("name", trim(lower(col("name"))))
df_clean.show()
