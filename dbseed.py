#!/usr/bin/python

import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'postgres'
password = 'secret'
database = 'test'

#creates db
connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor(cursor_factory=RealDictCursor)

#drop tables if exists...?
# cursor.execute('CREATE DATABASE test;')

cursor.execute('''
	DROP TABLE IF EXISTS 'procedures';
	''')

cursor.execute('''
	CREATE TABLE 'procedures' (
	'id' INTEGER PRIMARY KEY AUTO_INCREMENT DEFAULT NOT NULL,
	'id_procedure_types' INTEGER NULL DEFAULT NULL,
	'id_facilities' INTEGER NULL DEFAULT NULL,
	'tot_price' INTEGER NULL DEFAULT NULL,
	FOREIGN KEY (id_procedure_types) REFERENCES 'procedure_type' ('id'),
	FOREIGN KEY (id_facilities) REFERENCES 'facilities' ('id')

	);

''')

cursor.execute('''
	DROP TABLE IF EXISTS 'procedure_type';
''')

cursor.execute('''
	CREATE TABLE 'procedure_type' (
	'id' INTEGER PRIMARY KEY AUTO_INCREMENT DEFAULT NOT NULL,
	'cpt_code' VARCHAR NULL DEFAULT NULL,
	'description' MEDIUMTEXT NULL DEFAULT NULL
	);

''')

cursor.execute('''
	DROP TABLE IF EXISTS 'facilities';
''')

cursor.execute('''
	CREATE TABLE 'facilities' (
	'id' INTEGER PRIMARY KEY AUTO_INCREMENT DEFAULT NOT NULL,
	'name' MEDIUMTEXT NULL DEFAULT NULL,
	'address' MEDIUMTEXT NULL DEFAULT NULL,
	'image' BLOB NULL DEFAULT NULL,
	'reviews' MEDIUMTEXT NULL DEFAULT NULL
	);
''')

cursor.execute('''
	DROP TABLE IF EXISTS 'geolcations';
''')

cursor.execute('''
	CREATE TABLE 'geolocations' (
	'id' INTEGER PRIMARY KEY AUTO_INCREMENT DEFAULT NOT NULL,
	'id_facilities' INTEGER NULL DEFAULT NULL,
	'latitude' VARCHAR NULL DEFAULT NULL,
	'longitude' VARCHAR NULL DEFAULT NULL,
	FOREIGN KEY (id_facilities) REFERENCES 'facilities' ('id')
	);
''')

cursor.execute('''
''')



connection.commit()
connection.close()


 
# if __name__ == "__main__":
# 	main()







