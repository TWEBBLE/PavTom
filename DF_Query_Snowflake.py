from sqlalchemy import create_engine
from Snowflake_Connector import Snowflake_Connector
import os
import pandas as pd
from pathlib import Path
from snowflake.sqlalchemy import URL

snowflake_connection_details = {
    "user": os.environ.get('SNOWFLAKE_USER'),
    "role": os.environ.get('SNOWFLAKE_ROLE', "SYSADMIN"),
    "password": os.environ.get('SNOWFLAKE_PASSWORD'),
    "account": str(os.environ.get('SNOWFLAKE_ACCOUNT')) + "." + os.environ.get('SNOWFLAKE_REGION', "eu-west-1"),
    "warehouse": os.environ.get('SNOWFLAKE_WAREHOUSE', "COMPUTE_WH")
}

engine = create_engine(
    f'snowflake://{snowflake_connection_details["user"]}:{snowflake_connection_details["password"]}@{snowflake_connection_details["account"]}/WORLD_CUPS_DEV'
    )

df = pd.read_csv(f"{Path.cwd()}/WorldCupPlayers.csv")

print(df)

df.to_sql('players', engine, if_exists='replace',
          schema='MATCHES', index=False, chunksize=16000)
