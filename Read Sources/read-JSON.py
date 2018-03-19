#Let's query the data with Spark SQL, by first importing SparkContext and SQLContext:
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row

sc
sc.master
sqlc = SQLContext(sc)

twts_sql_df_01 = sqlc.read.json("jSON.json")
