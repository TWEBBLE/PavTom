# Pav & Tom's Data Engineering Project

In this project we're going to connect the code on our machines with our snowflake database using Python. This will involve writing a program that will act as a mediator between our terminals and snowflake.

## How to run the code
This project relies on environment variables for user authentication. You will need to export the following variables to your shell:

    SNOWFLAKE_USER
    SNOWFLAKE_ROLE
    SNOWFLAKE_PASSWORD
    SNOWFLAKE_ACCOUNT
    SNOWFLAKE_REGION
    SNOWFLAKE_WAREHOUSE

### To run the code use:

>python3 query_snowflake.py

This will populate your database on snowflake with data on every match in FIFA World Cup history.
