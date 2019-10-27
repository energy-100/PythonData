#import mmh3
from bitarray import bitarray
import pandas as pd
import numpy as np
import jsonpath
from pyspark.sql import SparkSession
spark = SparkSession \
     .builder \
     .config("spark.debug.maxToStringFields",1000) \
     .appName("BloomFilter") \
     .getOrCreate()
print('SessionCreate')
# spark.sparkContext.config
data_from_json = spark.read.json('netflow.json')
#print(data_from_json.take(1))
data_from_json.printSchema()
