# main.py

from pyspark.sql import SparkSession
from sys import path
from time import time

path.insert(0, "/app")


def myjob(spark: SparkSession, **kwargs):
    """
    myjob

    Main entrypoint for PySpark job

    INPUTS:
        spark - active SparkSession
        **kwargs - keyword arguments from spark-submit

    """
    df = spark.read.csv("spark-data/climatewatch-usemissions.csv")

    df.show()


if __name__ == "__main__":

    spark = (
        SparkSession
            .builder
            .appName("exercise")
            .master("spark://spark-master:7077")
            .getOrCreate()
    )

    start = time()
    myjob(spark)
    end = time()

    print(f"\nExecution of job took {end-start:.8f} seconds\n")
