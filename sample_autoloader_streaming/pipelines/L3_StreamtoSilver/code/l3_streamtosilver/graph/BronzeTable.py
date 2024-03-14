from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l3_streamtosilver.config.ConfigStore import *
from l3_streamtosilver.udfs.UDFs import *

def BronzeTable(spark: SparkSession) -> DataFrame:
    return spark.readStream.format("delta").load("dbfs:/tmp/incrementalETL/bronze/")
