from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l2_autoloader_read.config.ConfigStore import *
from l2_autoloader_read.udfs.UDFs import *

def LandingZone_Stream(spark: SparkSession) -> DataFrame:
    return spark.readStream\
        .format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .option("cloudFiles.schemaLocation", "dbfs:/tmp/incrementalETL/bronze/schema/")\
        .option("header", True)\
        .option("sep", ",")\
        .schema(
          StructType([
            StructField("date", StringType(), True), StructField("stock_symbol", StringType(), True), StructField("analyst", LongType(), True), StructField("estimated_eps", DoubleType(), True)
        ])
        )\
        .load("dbfs:/tmp/incrementalETL/LandingZone/")
