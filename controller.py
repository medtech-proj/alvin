from flask import Flask, redirect, render_template, session, request, url_for
import search
# from search import get_procedure_info
# import alvin_geos
import json

app = Flask(__name__)

#secret key assignment
# app.config['SECRET_KEY'] = open('secret_key', "rb").read()

#STATIC FUNCTIONS
def get_geojson(data):
	hospital=[]
	geo_json = {'type':"FeatureCollection", "features":hospital}

	for obj in data:
		hospital.append(
			{"geometry": 
				{"type": "Point",
				"coordinates": [obj["longitude"], obj['latitude']]
				},
			"id": str(obj['id']),
			# "properties": {
			# 	"marker-color": "#7e7e7e",
			# 	"marker-size": "medium",
			# 	"marker-symbol": "",
			# 	"object": "hi"
			# 	},
				"type": "Feature"
			})
			


	return geo_json
	# geo_json['features'].append(obj)


def get_json_details(data):
	details = []
	for i in data:
		details.append(
			{"name":i['name'],
			"lng": i["longitude"],
			"lat": i["latitude"],
			"price": i["tot_price"],
			"address": i['address'],
			"description":i['description'],
			"cpt_code":i['cpt_code'],
			"image":i['image'],
			"rating":i['rating'],
			"reviews":i['reviews']
			}
		)
	return details

	



@app.route("/")
def show_healthmap():
	# return render_template("healthmap.html")
	return render_template("map.html")

@app.route("/procedure/<name>")
def get_data(name):
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






if __name__ == "__main__":
	app.run(host="127.0.0.1", debug=True, port=5000)