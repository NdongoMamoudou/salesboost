# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType
import redis

# Create SparkSession
spark = SparkSession.builder \
    .appName("UserEventsStreaming") \
    .config("spark.sql.shuffle.partitions", "2") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("✅ Spark Streaming started... Listening Kafka topic: user_events")

# Kafka message schema
schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("product_id", StringType()) \
    .add("event_type", StringType()) \
    .add("timestamp", DoubleType())


# Score function
def score_event(event_type):
    if event_type == "buy": return 10
    if event_type == "click": return 4
    if event_type == "view": return 2
    return 1


# ✅ Processing Kafka events → Redis
def process_row(row):

    # ✅ Redis instance created inside worker (avoid pickle error)
    r = redis.Redis(host="redis", port=6379, decode_responses=True)

    score_value = score_event(row.event_type)

    # ✅ Global score by product
    r.incrby(f"product:{row.product_id}:score", score_value)

    # ✅ Personalized score per user (ZSET)
    r.zincrby(f"user:{row.user_id}:scores", score_value, row.product_id)

    print(f"🔥 Redis updated: user:{row.user_id}, product:{row.product_id}, +{score_value}")


# Read Kafka stream → apply logic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "user_events") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = json_df.writeStream \
    .foreach(process_row) \
    .start()

query.awaitTermination()
