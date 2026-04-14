from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# 1. Crear sesión de Spark con soporte Kafka
spark = SparkSession.builder \
    .appName("KafkaStreamingMovilidad") \
    .getOrCreate()

# 2. Leer datos desde Kafka
df_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "movilidad") \
    .load()

# 3. Convertir el valor de Kafka a string
df_stream = df_stream.selectExpr("CAST(value AS STRING)")

# 4. Procesamiento simple: contar eventos por valor recibido
agg_stream = df_stream.groupBy("value").count()

# 5. Mostrar resultados en consola en tiempo real
query = agg_stream.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()

