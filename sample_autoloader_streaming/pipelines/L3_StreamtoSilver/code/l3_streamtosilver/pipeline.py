from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from l3_streamtosilver.config.ConfigStore import *
from l3_streamtosilver.udfs.UDFs import *
from prophecy.utils import *
from l3_streamtosilver.graph import *

def pipeline(spark: SparkSession) -> None:
    df_BronzeTable = BronzeTable(spark)
    SilverTable(spark, df_BronzeTable)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/L3_StreamtoSilver")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L3_StreamtoSilver", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/L3_StreamtoSilver")

    pipeline(spark)
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
