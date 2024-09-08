from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# spark is an existing SparkSession
df = spark.read.json("C:\Programy\spark-3.5.2-bin-hadoop3\examples/src/main/resources/people.json")
# Displays the content of the DataFrame to stdout
df.show()

spark.stop()