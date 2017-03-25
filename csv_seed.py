#!/usr/bin/python

import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import numpy as np


hostname = 'localhost'
username = 'postgres' #postgres is the owner in psql 
password = 'secret'
database = 'test'

#creates db
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor(cursor_factory=RealDictCursor)

# cursor.execute('CREATE DATABASE test;')

#higher order function, replaces np.nan with ''
def replace_nan(default):
	def _replace(value):
		return default if value is np.nan else value
	return _replace

#pandas reads csv, calls replace
df = pd.read_csv(
	filepath_or_buffer='./combined_seed_tables.csv',
	converters={
		"name": replace_nan(''),
		"address": replace_nan(''),
		"image":replace_nan(''),
		"rating": replace_nan(0),
		"reviews": replace_nan(0),
		"cpt_code": replace_nan(0),
		"description": replace_nan(''),
		"tot_price": replace_nan(0)
	}
)

#connect to psql - (%(col)s) formatting specific to psql
#not using ORM 
#numpy converting column and values into dict
cursor.executemany('''
		INSERT INTO 
		facilities (name, address, image, rating, reviews) 
		VALUES
		(%(name)s,%(address)s,%(image)s,%(rating)s,%(reviews)s);
	''', 
	df.to_dict(orient="records")
)

cursor.executemany('''
		INSERT INTO 
		procedure_type (cpt_code, description) 
		VALUES
		(%(cpt_code)s,%(description)s);
	''', 
	df.to_dict(orient="records")
)

cursor.executemany('''
		INSERT INTO 
		procedures (tot_price) 
		VALUES
		(%(tot_price)s);
	''', 
	df.to_dict(orient="records")
)


connection.commit()
connection.close()
