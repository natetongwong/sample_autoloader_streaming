from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l1_prep_data.config.ConfigStore import *
from l1_prep_data.udfs.UDFs import *

def Repartition_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.repartition(1)
