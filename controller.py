from flask import Flask, redirect, render_template, session, request, url_for
import search
import json
from flask.ext.heroku import Heroku

app = Flask(__name__)

heroku = Heroku(app)

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
	# returns data formated to string to pass into http request, to be parsed into a JSON obj in the JS file as the this.responseText.


if __name__ == "__main__":
	app.run(host="127.0.0.1", debug=True, port=5000)