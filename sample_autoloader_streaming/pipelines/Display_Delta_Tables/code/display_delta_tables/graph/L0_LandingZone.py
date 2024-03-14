from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from display_delta_tables.config.ConfigStore import *
from display_delta_tables.udfs.UDFs import *

def L0_LandingZone(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("date", StringType(), True), StructField("stock_symbol", StringType(), True), StructField("analyst", LongType(), True), StructField("estimated_eps", DoubleType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/tmp/incrementalETL/LandingZone/")
