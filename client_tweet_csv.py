from pyspark.sql import SparkSession
from pyspark.sql import functions as f
import shutil

for item in ['D:\Romario\Programar\Alura\spark\streaming\check', 'D:\Romario\Programar\Alura\spark\streaming\csv']: 
    try: 
            shutil.rmtree(item)
    except OSError as err:
            print(f'Aviso: {err.strerror}')

spark=SparkSession.builder.appName("SparkStreaming").getOrCreate()

tweets= spark.readStream\
    .format('socket')\
        .option('host','localhost')\
            .option('port','9009')\
                .load()


query=tweets.writeStream\
    .outputMode('append')\
        .option('encoding','utf-8')\
            .format('csv')\
                .option('path','D:\Romario\Programar\Alura\spark\streaming\csv')\
                    .option('checkpointLocation','D:\Romario\Programar\Alura\spark\streaming\check')\
                        .start()
            
query.awaitTermination()