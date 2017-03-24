#!/usr/bin/python

import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import numpy as np
import json

hostname = 'localhost'
username = 'vince' #postgres is the owner in psql 
password = 'secret'
database = 'test'

#creates db
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor(cursor_factory=RealDictCursor)

# cursor.execute('CREATE DATABASE test;')
def replace_nan(default):
	def _replace(value):
		return default if value is np.nan else value
	return _replace


df = pd.read_csv(
	filepath_or_buffer='./combined_seed_tables.csv',
	converters={
		"name": replace_nan(''),
		"address": replace_nan(''),
		"image":replace_nan(''),
		"rating": replace_nan(0),
		"reviews": replace_nan(0)
	}
)

# names=df['name']
# addresses=df['address']
# images=df['image']
# ratings=df['rating']
# reviews=df['reviews']

# thelist = []
# name_tuples = [i for i in names]
# address_tuples = [i for i in addresses]
# image_tuples = [i for i in images]
# rating_tuples = [i for i in ratings]
# review_tuples = [i for i in reviews]

# print(name_tuples)
# thelist.append(name_tuples)
# print(thelist)


# address_tuples = []
# for a,b,c,d,e in zip(names, addresses, images, ratings, reviews):
# 	cursor.execute('''
# 		INSERT INTO 
# 		facilities (name, address, images, rating, reviews) 
# 		VALUES
# 		(%(a)s,%(b)s,%(c)s,%(d)s,%(e)s);
# 	''', {"a":a,"b":b,"c":c,"d":d,"e":e})


# cursor.executemany('''
# 		INSERT INTO 
# 		facilities (name, address, image, rating, reviews) 
# 		VALUES
# 		(%s,%s,%s,%s,%s);
# 	''', 
# 	(
# 		(
# 			name, 
# 			address, 
# 			('' if np.nan is image else image), 
# 			(0 if np.nan is rating else float(rating)), 
# 			(0 if np.nan is reviews else float(reviews))
# 		) 
# 		for 
# 			name, address, image, rating, reviews
# 		in 
# 			zip(names, addresses, images, ratings, reviews)
# 	)
# )

cursor.executemany('''
		INSERT INTO 
		facilities (name, address, image, rating, reviews) 
		VALUES
		(%(name)s,%(address)s,%(image)s,%(rating)s,%(reviews)s);
	''', 
	df.to_dict(orient="records")
)





cpt_codes=df['cpt_code']
descriptions=df['description']





tot_prices=df['tot_price']


connection.commit()
connection.close()
