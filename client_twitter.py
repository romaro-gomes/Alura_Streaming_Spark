from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark=SparkSession.builder.appName("SparkStreaming").getOrCreate()

lines= spark.readStream\
    .format('socket')\
        .option('host','localhost')\
            .option('port','9009')\
                .load()


word= lines.select(
        f.explode( # as organizam em forma de linhas
            f.split(lines.value," ") #Separa as palavras
                ).alias('word'))

word_counts=word.groupBy('word').count()
            


# query=lines.writeStream\
#     .outputMode('append')\
#         .format('console')\
#             .start()

query=word_counts.writeStream\
    .outputMode('complete')\
        .format('console')\
            .start()
            
query.awaitTermination()