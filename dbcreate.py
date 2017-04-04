#!/usr/bin/env python3

import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'Lisa' #postgres is the owner in psql 
password = 'secret'
database = 'test'

#creates db
connection = psycopg2.connect(dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor(cursor_factory=RealDictCursor)

# cursor.execute('CREATE DATABASE test;')

cursor.execute('''
	DROP TABLE IF EXISTS procedure_types CASCADE;
''')

cursor.execute('''
	CREATE TABLE procedure_types (
	id SERIAL PRIMARY KEY,
	cpt_code INTEGER,
	description TEXT
	);
''')

cursor.execute('''
	DROP TABLE IF EXISTS facilities CASCADE;
''')

cursor.execute('''
	CREATE TABLE facilities (
	id SERIAL PRIMARY KEY,
	name TEXT,
	address TEXT,
	image TEXT,
	rating REAL,
	reviews INTEGER
	);
''')

cursor.execute('''
	DROP TABLE IF EXISTS geolocations CASCADE;
''')

cursor.execute('''
	CREATE TABLE geolocations (
	id SERIAL PRIMARY KEY,
	id_facilities INTEGER,
	latitude REAL,
	longitude REAL,
	FOREIGN KEY (id_facilities) REFERENCES facilities(id)
	);
''')


cursor.execute('''
	DROP TABLE IF EXISTS procedures CASCADE;
	''')

cursor.execute('''
	CREATE TABLE procedures (
	id SERIAL PRIMARY KEY,
	id_procedure_types INTEGER,
	id_facilities INTEGER,
	tot_price INTEGER,
	FOREIGN KEY (id_procedure_types) REFERENCES procedure_types(id),
	FOREIGN KEY (id_facilities) REFERENCES facilities(id)
	);
''')


connection.commit()
connection.close()


 
# if __name__ == "__main__":
# 	main()







