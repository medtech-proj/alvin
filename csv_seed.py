import psycopg2
from psycopg2.extras import RealDictCursor
import csv


database = 'test'
connection = psycopg2.connect(dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()


with open("facilities.csv") as facilities_data:
	f = csv.reader(facilities_data)
	for row in f:
		# print(row)
		cursor.execute('''
			INSERT INTO
			facilities (name, address, image, rating, reviews)
			VALUES
			(%s,%s,%s,%s,%s);
		''', row)


with open("procedure_types.csv") as procedure_types_data:
	f = csv.reader(procedure_types_data)
	for row in f:
		# print(row)
		cursor.execute('''
			INSERT INTO
			procedure_types (cpt_code, description)
			VALUES
			(%s,%s);
		''', row)


with open("procedures.csv") as procedures_data:
	f = csv.reader(procedures_data)
	for row in f:
		# print(row)
		cursor.execute('''
			INSERT INTO
			procedures (id_procedure_types, id_facilities, tot_price)
			VALUES
			(%s,%s,%s);
		''', row)


connection.close()
