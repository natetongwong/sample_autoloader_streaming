from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from l2_autoloader_read.config.ConfigStore import *
from l2_autoloader_read.udfs.UDFs import *
from prophecy.utils import *
from l2_autoloader_read.graph import *

def pipeline(spark: SparkSession) -> None:
    df_LandingZone_Stream = LandingZone_Stream(spark)
    BronzeTable(spark, df_LandingZone_Stream)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/L2_autoloader_read")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L2_autoloader_read", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L2_autoloader_read")

    pipeline(spark)
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
