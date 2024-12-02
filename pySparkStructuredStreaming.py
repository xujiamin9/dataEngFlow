import os
import sys
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F
from pyspark.sql.functions import *
from pyspark.sql.types import *

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# Create the Spark Session

spark = SparkSession \
    .builder \
    .appName("Streaming from Kafka") \
    .config("spark.streaming.stopGracefullyOnShutdown", True) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0') \
    .config("spark.sql.shuffle.partitions", 4) \
    .master("local[*]") \
    .getOrCreate()

# Create the streaming_df to read from kafka
streaming_df = spark.readStream\
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "transactions") \
    .option("startingOffsets", "earliest") \
    .load()

# JSON Schema
from pyspark.sql.types import StringType, StructField, StructType, TimestampType,DoubleType, LongType

json_schema = StructType([StructField('transaction_id', StringType(), True), \
StructField('customer_name', StringType(), True), \
StructField('date', TimestampType(), True), \
StructField('amount', DoubleType(), True), \
StructField('description', StringType(), True), \
StructField('account_number', StringType(), True), \
StructField('merchant', StringType(), True), \
StructField('category', StringType(), True), \
StructField('eventId', StringType(), True), \
StructField('eventOffset', LongType(), True), \
StructField('eventPublisher', StringType(), True), \
StructField('eventTime', StringType(), True)])

# Parse value from binay to string
json_df = streaming_df.selectExpr("cast(value as string) as value")

# Apply Schema to JSON value column and expand the value
from pyspark.sql.functions import from_json

json_expanded_df = json_df.withColumn("value", from_json(json_df["value"], json_schema)).select("value.*")

print('test')

def write_streaming(df, epoch_id):
    df.write \
        .format("jdbc") \
        .mode("append") \
        .option("url", f"jdbc:postgresql://localhost:5432/postgres") \
        .option("dbtable", "transactions") \
        .option("user", 'postgres') \
        .option("password", 'postgres') \
        .option("driver", "org.postgresql.Driver")\
        .save()
    print("data loaded")

# Define a query to postgre table: employees


streaming_query = json_expanded_df.writeStream \
    .foreachBatch(write_streaming) \
    .start()\
    .awaitTermination()


