from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from display_delta_tables.config.ConfigStore import *
from display_delta_tables.udfs.UDFs import *

def L1_BronzeTable(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/tmp/incrementalETL/bronze")
