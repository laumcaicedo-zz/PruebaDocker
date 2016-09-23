from flask import Flask, url_for, redirect
from flask import render_template
from flask import request
import sys
import optparse
import time
import os


app = Flask(__name__)

start = int(round(time.time()))

@app.route('/')
def hello():
    return render_template ("Choosing_Service.html") 

@app.route('/RU',methods=['GET', 'POST'])
def RU():
	if request.method == 'GET':
		return render_template ("Choosing_Server.html")  
	elif request.method == 'POST':
		RackUnit=request.form['submittedAnswer'];
		if RackUnit == '1':
			return "You need a C220";
		elif RackUnit == '2':
			return "You need a C240";
		elif RackUnit == '4':
			return ("a"+ url("http://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/c460m4_specsheet.pdf"));
@app.route('/CPU')
def Rack_units():
	return render_template ("Choosing_CPU.html.html")  

if __name__ == "__main__":
	port= int(os.environ.get('PORT',5002))
	app.run(host='0.0.0.0', port=port)