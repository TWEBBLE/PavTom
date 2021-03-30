from sqlalchemy import create_engine
import os
import pandas as pd

from Snowflake_Connector import snowflake_connection_details
from pathlib import Path
from snowflake.sqlalchemy import URL
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

snowflake_connection_details = snowflake_connection_details()

engine = create_engine(
    URL(
        account=snowflake_connection_details["account"],
        user=snowflake_connection_details["user"],
        password=snowflake_connection_details["password"],
        role=snowflake_connection_details["role"],
        warehouse=snowflake_connection_details["warehouse"],
        database="WORLD_CUPS_DEV",
        schema="MATCHES",
    )
)

df = pd.read_csv(f"{Path.cwd()}/WorldCupPlayers.csv")

try:
    connection = engine.connect()
    df.to_sql(
        "players",
        engine,
        if_exists="replace",
        schema="MATCHES",
        index=False,
        chunksize=16000,
    )
    print(result)
finally:
    connection.close()
    engine.dispose()
