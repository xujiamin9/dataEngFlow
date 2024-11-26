import os
import sys
from pyspark.sql import SparkSession


os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.master("local").appName("PySpark Installation Test").getOrCreate()
df = spark.createDataFrame([(1, "Hello"), (2, "World")], ["id", "message"])
df.show()
