from flask import Flask, redirect, render_template, session, request, url_for
import search
import json

app = Flask(__name__)

#secret key assignment
# app.config['SECRET_KEY'] = open('secret_key', "rb").read()

@app.route("/")
def show_healthmap():
	return render_template("map.html")


@app.route("/procedure/<name>")
def get_data(name):
	# data = search.py function get_procedure_info from passed in name to the SQL query. data is a cursor.fetchall() (list of tuples)
	data = search.get_procedure_info(name)
	
	return json.dumps(data)
	# returns data formated to json, to be parsed in the JS file as the this.responseText. it is an array of objects.


#STATIC FUNCTIONS
# def get_json_details(data):
# 	print(data)
# 	details = []
# 	for i in data:
# 		details.append(
# 			{"name":i['name'],
# 			"lng": i["longitude"],
# 			"lat": i["latitude"],
# 			"price": i["tot_price"],
# 			"address": i['address'],
# 			"description":i['description'],
# 			"cpt_code":i['cpt_code'],
# 			"image":i['image'],
# 			"rating":i['rating'],
# 			"reviews":i['reviews']
# 			}
# 		)
# 	return details



if __name__ == "__main__":
	app.run(host="127.0.0.1", debug=True, port=5000)
	