## Code to test things

from pyspark.sql import functions as F

path_checkpoint = "dbfs:/user/mayank.srivastava@frieslandcampina.com/dbacademy/adewd/0/_checkpoints"


def update_silver():
    query = (spark.readStream
             .table("bronze")
             .withColumn("processed_time", F.current_timestamp())
             .writeStream.option("checkpointLocation", f"{path_checkpoint}/silver")
             .trigger(availableNow=True)
             .table("silver")
             )
    
    query.awaitTermination()


update_silver()