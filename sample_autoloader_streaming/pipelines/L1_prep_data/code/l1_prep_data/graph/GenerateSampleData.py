from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from l1_prep_data.config.ConfigStore import *
from l1_prep_data.udfs.UDFs import *

def GenerateSampleData(spark: SparkSession) -> DataFrame:
    out0 = spark.createDataFrame(
        [('3/1/2021', 'a', 1, 2.2), ('3/1/2021', 'a', 2, 2.0), ('3/1/2021', 'b', 1, 1.3), ('3/1/2021', 'b', 2, 1.2),
         ('3/1/2021', 'c', 1, 3.5), ('3/1/2021', 'c', 2, 2.6)],
        ('date', 'stock_symbol', 'analyst', 'estimated_eps')
    )

    return out0
