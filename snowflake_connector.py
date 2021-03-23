import snowflake.connector
from snowflake.connector import DictCursor
import pandas as pd
import os


class SnowflakeConnector:
    def __init__(self, connection_parameters):
        self.connection_parameters = connection_parameters

    def open_connection(self):
        try:
            connection = snowflake.connector.connect(**self.connection_parameters)
            return connection
        except Exception as Error_returned:
            raise RuntimeError(
                "Snowflake Connection",
                f"Error connecting to Snowflake: {Error_returned}",
            )

    def set_session_parameters(self, role: str, warehouse: str):
        cursor = self.open_connection().cursor(DictCursor)
        try:
            cursor.execute(f"USE ROLE {role};")
            cursor.execute(f"USE WAREHOUSE {warehouse};")
            return cursor
        except Exception as error_returned:
            raise RuntimeError(
                f"Setting the Role and Warehouse threw error: {error_returned}"
            )

    def run_sql(self, cursor: snowflake.connector.DictCursor, sql_statements: str):
        try:
            cursor.execute(sql_statements)
            rows_returned = [row for row in cursor]
            return rows_returned
        except Exception as error_returned:
            raise RuntimeError(
                f"SQL statements: {sql_statements}\n threw error {error_returned}"
            )

    def fetch_dataframe_from_sql(
        self, cursor: snowflake.connector.cursor.DictCursor, sql_query: str
    ):
        try:
            query_result = cursor.execute(sql_query)
            df = pd.DataFrame.from_records(
                iter(query_result), columns=[row[0] for row in query_result.description]
            )
            return df
        except Exception as error_returned:
            raise RuntimeError(
                f"SQL statement: {sql_query}\n threw error: {error_returned}"
            )

    def closer_cursor(self, cursor):
        cursor.close()


def snowflake_connection_details():
    snowflake_connection_details = {
        "user": os.environ.get("SNOWFLAKE_USER"),
        "role": os.environ.get("SNOWFLAKE_ROLE", "SYSADMIN"),
        "password": os.environ.get("SNOWFLAKE_PASSWORD"),
        "account": str(os.environ.get("SNOWFLAKE_ACCOUNT"))
        + "."
        + os.environ.get("SNOWFLAKE_REGION", "eu-west-1"),
        "warehouse": os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
    }
    return snowflake_connection_details
