from flask import Flask, redirect, render_template, session, request, url_for
# import model

app = Flask(__name__)

#secret key assignment
# app.config['SECRET_KEY'] = open('secret_key', "rb").read()

@app.route("/")
def show_healthmap():
	
	# return render_template("healthmap.html")
	return render_template("map.html")

@app.route("/procedure/<name>")
def get_hos_name():
	data=query(name)
	# return httpResponse(json.dumps(data))
	return json.dumps(data)



if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000)