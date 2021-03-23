from snowflake_connector import snowflake_connection_details
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env_test"
load_dotenv(dotenv_path=env_path)


def test_snowflake_connection_details():
    assert snowflake_connection_details() == {
        "user": "A",
        "role": "B",
        "password": "C",
        "account": "D.E",
        "warehouse": "F",
    }
