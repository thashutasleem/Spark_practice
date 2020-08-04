import sys
import os
from py4j.java_gateway import java_import, JavaObject
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def main():
    sc = SparkContext(master="local[2]",appName="pysparkStreaming")
    ssc = StreamingContext(sc, 20)
    lines = ssc.socketTextStream('localhost',2222)
    words_count = lines.flatMap(lambda line: line.split(" "))\
    .map(lambda word: (word, 1))\
    .reduceByKey(lambda x, y: x + y)
    words_count.pprint()
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    main()
