from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l3_streamtosilver.config.ConfigStore import *
from l3_streamtosilver.udfs.UDFs import *

def SilverTable(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("delta")\
        .option("checkpointLocation", "dbfs:/tmp/incrementalETL/silver/checkpoint.")\
        .queryName("StreamingTarget_1_6UIpLMsjy5MGRG0W6f5Si$$CXk-ZmxjSHrsV_lzki2X2")\
        .outputMode("append")\
        .trigger(once = True)\
        .start("dbfs:/tmp/incrementalETL/silver")
