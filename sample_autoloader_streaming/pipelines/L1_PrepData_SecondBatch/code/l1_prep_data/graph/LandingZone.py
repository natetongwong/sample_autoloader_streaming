from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l1_prep_data.config.ConfigStore import *
from l1_prep_data.udfs.UDFs import *

def LandingZone(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("append")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/tmp/incrementalETL/LandingZone/")
