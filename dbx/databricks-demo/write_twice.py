from pyspark.sql import functions as F

path_checkpoint = "dbfs:/user/mayank.srivastava@frieslandcampina.com/dbacademy/adewd/0/_checkpoints"

def write_twice(microBatchDF, batchId):
    app_id = "write_twice"

    microBatchDF.select("id", "name", F.current_timestamp().alias("processed_time")).write.option(
        "txnVersion", batchId).option("txnAppId", app_id).mode("append").saveAsTable("silver_name")
    
    microBatchDF.select("id", "value", F.current_timestamp().alias("processed_time")).write.option(
        "txnVersion", batchId).option("txnAppId", app_id).mode("append").saveAsTable("silver_value")
    

def split_stream(): 
    query = (spark.readStream.table("bronze")
                .writeStream
                .foreachBatch(write_twice)
                .option("checkpointLocation", f"{path_checkpoint}/split_stream")
                .trigger(availableNow=True)
                .start())
    
    query.awaitTermination()


split_stream()