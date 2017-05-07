from flask import Flask, redirect, render_template, session, request, url_for
from search import get_cpt_info, get_procedure_info
import json

app = Flask(__name__)


#secret key assignment
# app.config['SECRET_KEY'] = open('secret_key', "rb").read()

@app.route("/")
def show_healthmap():
	return render_template("map.html")


@app.route("/procedure/<name>")
def get_data(name):

	name=name.replace('+', '/')
	# data = search.py function get_procedure_info from passed in name to the SQL query. data is a cursor.fetchall() (list of tuples)
	data = get_procedure_info(name)
	
	return json.dumps(data)
	# returns data formated to string to pass into http request, to be parsed into a JSON obj in the JS file as the this.responseText.

@app.route("/cpt/<num>")
def get_code(num):
	# data = search.py function get_procedure_info from passed in name to the SQL query. data is a cursor.fetchall() (list of tuples)
	data = get_cpt_info(num)
	
	return json.dumps(data)
	# returns data formated to string to pass into http request, to be parsed into a JSON obj in the JS file as the this.responseText.


if __name__ == "__main__":
	app.run(host="127.0.0.1", debug=True, port=5000)