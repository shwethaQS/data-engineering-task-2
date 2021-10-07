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

The exercise is in two parts. In the first, we'd like you to perform a number of manipulations of the provided dataset. In the second, we'd like you to demonstrate your ability to extend the infrastructure and output the data.

### Part 1

The data file `spark-data/climatewatch-usemissions.csv` has already been read into a DataFrame in the example job. It is a dataset consisting of emissions data for US states provided and maintained by the World Resources Institute's [Climate Watch project](http://cait.wri.org/).

We would like you to

1. - filter the data to show just the emissions for California by year
   - display the result
2. - filter the data to show just the emissions for 2018
   - create new column total N2O emissions / population
   - order by this per-capita column
   - display the output
3. - group the data by year
   - sum the emissions data
   - display the total US emissions figures by year
4. - using the data in `spark-data/regions-divisions.json`...
   - create a new column, 'region', indicating the state's region
   - group by region _and_ year to get regional time series (similar to the original data with 'region' replacing 'state')
   - display the output

### Part 2

So far we have asked you to manipulate data in the Spark cluster and display the output in the terminal. In this part of the exercise we will ask you to add a database container via `docker-compose.yml` and read out the results of your previous work into appropriate database tables.

1. take the cluster down and add a `postgres` container to the docker compose configuration. You should make sure you'll be able to access a database and persist the data when the container is stopped.
2. spin the cluster up. Take whatever steps are necessary to connect to the database from inside the cluster.
3. export the data from the previous steps to appropriate database tables

Further Information
-------------------

The column names of the provided CSV are as follows:

```
"Index"
"State"
"Year"
"Total GHG Emissions Excluding LUCF (MtCO2e)"
"Total GHG Emissions Including LUCF (MtCO2e)"
"Total CO2 (excluding LUCF) (MtCO2e)"
"Total CH4 (MtCO2e)"
"Total N2O (MtCO2e)"
"Total F-Gas (MtCO2e)"
"Energy (MtCO2e)"
"Industrial Processes (MtCO2e)"
"Agriculture (MtCO2e)"
"Waste (MtCO2e)"
"Land Use and Forestry (MtCO2e)"
"Bunker Fuels (MtCO2e)"
"Electric Power (MtCO2e)"
"Commercial (MtCO2e)"
"Residential (MtCO2e)"
"Industrial (MtCO2e)"
"Transportation (MtCO2e)"
"Fugitive Emissions (MtCO2e)"
"State GDP (Million US$ (chained 1997/2005))"
"Population (People)"
"Total Energy Use (Thous. tonnes oil eq. (ktoe))"
```
