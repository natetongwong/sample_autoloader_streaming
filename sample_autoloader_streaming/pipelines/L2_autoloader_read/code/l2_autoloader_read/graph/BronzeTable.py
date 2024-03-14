from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l2_autoloader_read.config.ConfigStore import *
from l2_autoloader_read.udfs.UDFs import *

def BronzeTable(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("delta")\
        .option("checkpointLocation", "dbfs:/tmp/incrementalETL/bronze/checkpoint/")\
        .queryName("BronzeTable_hnSBMANK8UNrF3yop28Bx$$2MkgJ1X3WPHZtTzVcMcoP")\
        .outputMode("append")\
        .trigger(once = True)\
        .start("dbfs:/tmp/incrementalETL/bronze/")
