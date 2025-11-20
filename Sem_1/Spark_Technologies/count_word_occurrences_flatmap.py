from pyspark import SparkConf, SparkContext

# Create Spark configuration and context
conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

# Read input text file
input = sc.textFile("book.txt")

# Split each line into words
words = input.flatMap(lambda x: x.split())

# Count frequency of each word
wordCounts = words.countByValue()

# Print results, ignoring non-ASCII characters
for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if cleanWord:
        print(cleanWord.decode() + " " + str(count))
