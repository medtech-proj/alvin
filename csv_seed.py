import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import numpy as np

#pandas reads csv, calls replace
facilities_df = pd.read_csv('./facilities.csv')
procedure_types_df = pd.read_csv('./procedure_types.csv')
procedures_df = pd.read_csv('./procedures.csv')


database = 'test'
connection = psycopg2.connect(dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()#cursor_factory=RealDictCursor)




cursor.executemany('''
    INSERT INTO
    facilities (name, address, image, rating, reviews)
        VALUES
    (%(name)s,%(address)s,%(image)s,%(rating)s,%(reviews)s);
''',
df.to_dict(orient="records")