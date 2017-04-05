#!/usr/bin/env python3

import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import numpy as np


hostname = 'localhost'
username = 'Lisa' #postgres is the owner in psql 
password = 'secret'
database = 'test'

#creates db
# connection = psycopg2.connect(host=hostname, user=username, dbname=database)
connection = psycopg2.connect(dbname=database)

#create cursor factory
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = connection.cursor()#cursor_factory=RealDictCursor)



cursor.execute('''
		INSERT INTO 
		facilities (name, address, image, rating, reviews) 
		VALUES
		('New York-Presbyterian Weill Cornell Medical Center', '525 E 68th St, New York, NY 10065','image blob', 4.8, 12),
		('NYU Langone Medical Center', '550 1st Avenue, New York, NY 10016', 'blob', 3.7, 99),
		('NYC Health + Hospitals/Metropolitan', '1901 1st Avenue, New York, NY 10029', 'image link', 3.4, 131),
		('Bellevue Hospital Center', '462 1st Avenue, New York, NY 10016', 'blob', 3.5, 314),
		('New York Presbyterian Hospital', '650 W 168th St, New York, NY 10032', 'image', 3.3, 33),
		('Mount Sinai Beth Israel', '10 Nathan D Perlman Pl, New York, NY 10003', 'image', 3.6, 67)
		;''')

cursor.execute('''
		INSERT INTO 
		procedure_type (cpt_code, description) 
		VALUES
		(70470, 'CT Head W W/O Contrast'),
		(70553, 'MRI Brain W W/O Contrast'),
		(73610, 'X-Ray Ankle 3 views')
		;
	'''
)


cursor.execute('''
		INSERT INTO 
		procedures (cpt_code, facility_name, tot_price) 
		VALUES
		(70470, 'New York Presbyterian Hospital', 1000),
		(70470, 'Mount Sinai Beth Israel', 23451 ),
		(70553, 'New York-Presbyterian Weill Cornell Medical Center', 18151),
		(73610, 'New York-Presbyterian Weill Cornell Medical Center', 1234),
		(70470, 'NYU Langone Medical Center', 23975),
		(70553, 'Bellevue Hospital Center', 12375)
		;
	'''
)


connection.commit()
connection.close()

# INSERT INTO films SELECT * FROM tmp_films WHERE date_prod < '2004-05-07';
