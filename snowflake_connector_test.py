from DF_Query_Snowflake import snowflake_connection_details

def snowflake_test():
    
    assert snowflake_connection_details == {"user":"PAVJAGODA", "role":"SYSADMIN","password":"XXXXXXXXXX", "account":"ui70075.eu-west-1", "warehouse":"COMPUTE_WH"}
