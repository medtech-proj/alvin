import psycopg2
from psycopg2.extras import RealDictCursor


hostname = 'localhost'
username = 'Lisa' #postgres is the owner in psql 
password = 'secret'
database = 'test'


def get_procedure_info(procedure):
#creates db
	connection = psycopg2.connect(dbname=database)

#create cursor factory
	connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

	cursor = connection.cursor(cursor_factory=RealDictCursor)



# search =  "CT Head W W/O Contrast"


	# print(procedure)
	data = str(procedure)+'%'
	cursor.execute('''
		SELECT name, address, description, tot_price, image, rating, reviews
		FROM procedures 

		JOIN procedure_types
		ON procedure_types.id = procedures.id_procedure_types

		JOIN facilities 
		ON procedures.id_facilities = facilities.id

		WHERE procedure_types.description LIKE (%s);
	''', (data,))
	# print(data)
	query = cursor.fetchall()
	print(query)
	return query
	# return query

# get_procedure_info('CT')


	connection.close()


