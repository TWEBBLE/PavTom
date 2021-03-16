export ENV=DEV
echo deploying environment $ENV
python3 query_snowflake.py

export ENV=STAGING
echo deploying environment $ENV
python3 query_snowflake.py

export ENV=PROD
echo deploying environment $ENV
python3 query_snowflake.py
