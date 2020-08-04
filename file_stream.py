import sys
import os
from py4j.java_gateway import java_import, JavaObject
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def main():
    sc = SparkContext(appName="pysparkStreaming")
    ssc = StreamingContext(sc, 10)
    lines = ssc.textFileStream('files/')
    words_count = lines.flatMap(lambda line: line.split(" "))\
    .map(lambda word: (word, 1))\
    .reduceByKey(lambda x, y: x + y)
    words_count.pprint()
    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    main()
