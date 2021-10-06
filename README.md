data-engineering-task-2
=======================

A technical exercise for mid-level data engineers

Setup Instructions
------------------

- make sure you have installed `docker` and `docker-compose`
- run `docker-compose up`
- this should bring up four containers: a Spark 'master' node, two Spark 'worker' nodes, and a gateway container
- the last of these is to ensure that you're using compatible versions of python etc. when you try to submit pyspark jobs
- use `docker exec -it pyspark-gateway /bin/bash` to shell into the gateway container
- run `python src/main.py` to run the example job
- after a moment you should see the dataset loaded from `spark-data` displayed in the terminal

Exercise Instructions
---------------------

To follow shortly.
