from flask import Flask, redirect, render_template, session, request, url_for
import search
# from search import get_procedure_info
# import alvin_geos
import json

app = Flask(__name__)

#secret key assignment
# app.config['SECRET_KEY'] = open('secret_key', "rb").read()

@app.route("/")
def show_healthmap():
	
	# return render_template("healthmap.html")
	return render_template("map.html")

@app.route("/procedure/<name>")
def get_hosp_name(name):
	data = search.get_procedure_info(name)
	# return httpResponse(json.dumps(data))
	# for _ in data:
	for obj in data:
		x = obj['name']
		address = obj['address']
		description = obj['description']
		tot_price = obj['tot_price']
		image = obj['image']
		rating = obj['rating']
		reviews = obj['reviews']


		print(x)


	# print(data[0]['name'])
	# print(type(data))
	result = {'result':str(data)}

	return json.dumps(result)




if __name__ == "__main__":
	app.run(host="127.0.0.1", debug=True, port=5000)