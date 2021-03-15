from Snowflake_Connector import Snowflake_Connector
import os

snowflake_connection_details = {
    "user": os.environ.get('SNOWFLAKE_USER'),
    "role": os.environ.get('SNOWFLAKE_ROLE', "SYSADMIN"),
    "password": os.environ.get('SNOWFLAKE_PASSWORD'),
    "account": str(os.environ.get('SNOWFLAKE_ACCOUNT')) + "." + os.environ.get('SNOWFLAKE_REGION', "eu-west-1"),
    "warehouse": os.environ.get('SNOWFLAKE_WAREHOUSE', "COMPUTE_WH")
    }

snowflake_instance = Snowflake_Connector(snowflake_connection_details)
cursor = snowflake_instance.set_session_parameters( role="SYSADMIN", warehouse="COMPUTE_WH")
create_db_world_cups = snowflake_instance.run_sql(
    cursor, f"CREATE DATABASE IF NOT EXISTS World_Cups_{os.environ.get('ENV', 'DEV')};")
result = snowflake_instance.run_sql(cursor, "SHOW DATABASES;")
df = snowflake_instance.fetch_dataframe_from_sql(cursor, "SHOW DATABASES;")
print(df)

create_schema_matches = snowflake_instance.run_sql(
    cursor, f"CREATE SCHEMA IF NOT EXISTS World_Cups_{os.environ.get('ENV', 'DEV')}.Matches;")

table_ddl_statement =''' "Year" INTEGER, "Date" DATE, "Time" TIME, "Stage" VARCHAR(50), "Stadium" VARCHAR(50), "City" VARCHAR(50), "Home_Team_Name" VARCHAR(50), "Home_Team_Goals" INTEGER, "Away_Team_Goals" INTEGER, "Away_Team_Name" VARCHAR(50), "Win_conditions" VARCHAR(50), "Attendance" INTEGER, "Half_time_Home_Goals" INTEGER, "Half_time_Away_Goals" INTEGER, "Referee" VARCHAR(50), "Assistant_1" VARCHAR(50), "Assistant_2" VARCHAR(50), "RoundID" INTEGER, "MatchID" INTEGER, "Home_Team_Initials" VARCHAR(5), "Away_Team_Initials" VARCHAR(5) '''
create_table_Games = snowflake_instance.run_sql(
    cursor, f"CREATE TABLE IF NOT EXISTS World_Cups_{os.environ.get('ENV', 'DEV')}.Matches.games ({table_ddl_statement});")
data_putter = snowflake_instance.run_sql(
    cursor, f'PUT file://Data\WorldCupMatches.csv @~ auto_compress=false;')
read = snowflake_instance.run_sql(cursor, f"LIST @~")
print(read)

data_copier = snowflake_instance.run_sql(
cursor, f"""COPY INTO World_Cups_{os.environ.get('ENV', 'DEV')}.Matches.games from @~/WorldCupMatches.csv FILE_FORMAT = (TYPE = 'csv' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);""")

