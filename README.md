# Description

This project is meant to analyze the performance of database queries using different connection strategies
The script will run an insert sql query for a specified time with the following connection strategies:

1. A new connection will be created for each query
2. The same connection will be used for the entire duration of the test
3. A connection pool will be used, the queries will be run using a TH number of threads

# Expectations

* The first strategy will have the lowest number of total inserts due to the overhead from creating a new connection each time
* A single connection will have a significant larger number of total inserts compared to the first strategy
* The number of inserts / thread will be a bit lower than the above strategy due to synchronization, but overall a larger number 
of inserts due to an increased number of threads

# Usage

* To setup the database run:

        python main.py init

* All simulations will start by running:

        python main.py start --time <time_of_the_simulation_in_minutes> --threads <integer_number_of_threads> 