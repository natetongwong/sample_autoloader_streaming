from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from l1_prep_data.config.ConfigStore import *
from l1_prep_data.udfs.UDFs import *
from prophecy.utils import *
from l1_prep_data.graph import *

def pipeline(spark: SparkSession) -> None:
    df_GenerateSampleData = GenerateSampleData(spark)
    df_Repartition_1 = Repartition_1(spark, df_GenerateSampleData)
    LandingZone(spark, df_Repartition_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/L1_prep_data")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L1_prep_data", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L1_prep_data")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
