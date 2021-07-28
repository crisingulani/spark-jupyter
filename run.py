import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL: loading DES products metrics") \
    .getOrCreate()

#df_catdb = spark.read.json("data/catalogdb.json")
df_admdb = spark.read.json("data/admindb.json")
#df_file = spark.read.json("data/fileinfo.json")

df_admdb.printSchema()