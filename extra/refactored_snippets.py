		// google.maps.event.addListener(marker, "click", function(e) {
		// infoWindow.setContent(data[i]);
		// infoWindow.open(map, marker);
		// })


#STATIC FUNCTIONS in controller.py
# def get_geojson(data):
# 	hospital=[]
# 	geo_json = {'type':"FeatureCollection", "features":hospital}

# 	for obj in data:
# 		hospital.append(
# 			{"geometry": 
# 				{"type": "Point",
# 				"coordinates": [obj["longitude"], obj['latitude']]
# 				},
# 			"id": str(obj['id']),
# 			# "properties": {
# 			# 	"marker-color": "#7e7e7e",
# 			# 	"marker-size": "medium",
# 			# 	"marker-symbol": "",
# 			# 	"object": "hi"
# 			# 	},
# 				"type": "Feature"
# 			})
			


# 	return geo_json
# 	# geo_json['features'].append(obj)


@app.route("/procedure/<name>")
def get_data(name):
	# data = search.py function get_procedure_info passed in name to the SQL query
	data = search.get_procedure_info(name)

	# return httpResponse(json.dumps(data))
	# for _ in data:
	# for obj in data:
	# 	x = obj['name']
	# 	address = obj['address']
	# 	description = obj['description']
	# 	cpt_code = obj['cpt_code']
	# 	tot_price = obj['tot_price']
	# 	image = obj['image']
	# 	rating = obj['rating']
	# 	reviews = obj['reviews']
	# 	latitude = obj['latitude']
	# 	longitude = obj['longitude']

		# print(x)


	# print(data[0]['name'])
	# print(type(data))
	# geo_json=get_json_details(data)
	
	return json.dumps(data)
	# this is the responseText on javascript



joindb = select * from (SELECT * 
FROM procedures 
JOIN facilities 
ON procedures.facility_name = facilities.name
JOIN procedure_type
ON procedure_type.cpt_code = facilities.cpt_code) 




# Use bytearray:

with open("img.png", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

print b[0]



<p>geojson map</p>
    <script src="https://gist.github.com/lgibson212/54c45fdee464ad0fa6d707ac8626c96d.js"></script>

<p>gmaps, budapest</p>
	<iframe src="https://www.google.com/maps/d/u/0/embed?mid=161fwYY69xR1ndyz-nq8p8PATZhM" width="640" height="480"></iframe>


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






# #higher order function, replaces df Nans with ''
# def replace_nan(default):
# 	def _replace(value):
# 		return default if value is np.nan else value
# 	return _replace

# #pandas reads csv, calls replace
# df = pd.read_csv(
# 	filepath_or_buffer='./combined_seed_tables.csv',
# 	converters={
# 		"name": replace_nan(''),
# 		"address": replace_nan(''),
# 		"image":replace_nan(''),
# 		"rating": replace_nan(0),
# 		"reviews": replace_nan(0),
# 		"cpt_code": replace_nan(0),
# 		"description": replace_nan(''),
# 		"tot_price": replace_nan(0)
# 	}
# )

# names=df['name']
# addresses=df['address']
# images=df['image']
# ratings=df['rating']
# reviews=df['reviews']


#connect to psql - (%(col)s) formatting specific to psql
#not using ORM 
#numpy converting column and values into dict