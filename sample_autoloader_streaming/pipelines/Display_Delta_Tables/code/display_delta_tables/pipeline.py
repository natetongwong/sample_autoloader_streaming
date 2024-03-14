from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from display_delta_tables.config.ConfigStore import *
from display_delta_tables.udfs.UDFs import *
from prophecy.utils import *
from display_delta_tables.graph import *

def pipeline(spark: SparkSession) -> None:
    df_L0_LandingZone = L0_LandingZone(spark)
    df_L1_BronzeTable = L1_BronzeTable(spark)
    df_L2_SilverTable = L2_SilverTable(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Display_Delta_Tables")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Display_Delta_Tables", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Display_Delta_Tables")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
