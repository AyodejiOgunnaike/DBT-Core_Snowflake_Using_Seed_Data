import snowflake.connector

conn = snowflake.connector.connect(
    user='AyodejiOgunnaike',
    password='',
    account='qga42617.east-us-2.azure',
    role='ACCOUNTADMIN',
    warehouse='COMPUTE_WH',
    database='DATA_DB',
    schema='DATA_SCHEMA'
)

cur = conn.cursor()
cur.execute("GRANT SELECT ON ALL TABLES IN SCHEMA data_schema TO joseph;")
cur.close()
conn.close()