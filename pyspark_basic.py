import pyspark
from pyspark.sql import SparkSession

spark=SparkSession.builder.config("spark.driver.host", "localhost").appName('appname').getOrCreate()

print('Hello pyspark')
