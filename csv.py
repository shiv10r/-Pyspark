from pyspark.sql import SparkSession
spark=  SparkSession.builder.getOrCreate()
Spark
df= spark.read.csv("C:\\Users\\shiva\\Downloads\\archive (1)\\sales_data_sample.csv",
inferSchema = True, header =  True)
df.show()
df.printSchema()
df.Select("ORDERNUMBER
").show(5)