import pandas as pd
import psycopg2 as pg
# import pandas.io.sql as psql

connection = pg.connect("dbname=test")
addresses_df = pd.read_sql_query('SELECT address FROM "facilities"',connection)