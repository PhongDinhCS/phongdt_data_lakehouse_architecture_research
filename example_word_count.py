from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    # Create a SparkConf object and SparkContext
    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)

    # Read the input file
    input = sc.textFile("/tmp/example_hadoop.txt")

    # Perform the word count
    counts = input.flatMap(lambda line: line.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a + b)

    # Save the result to the output directory
    counts.saveAsTextFile("/tmp/output")

    # Stop the SparkContext
    sc.stop()
