# import all required packages
from flask import Flask, render_template, request
import tensorflow as tf
import keras
from keras.models import load_model
import pandas as pd

web_site = Flask(__name__)

model = load_model('model.h5') # load ML model

@web_site.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST': # if form is submitted

		# get all values from the form
		age = float(request.form["age"])
		sex = float(request.form["sex"])
		bp = float(request.form["bp"])
		exang = float(request.form["exang"])
		cp = float(request.form["cp"])
		chol = float(request.form["chol"])
		bs = float(request.form["bs"])
		caa = float(request.form["caa"])
		max_hr = float(request.form["max_hr"])

		# make a dataframe with all the inputs
		data = {'age': [age], 'sex': [sex], 'trtbps': [bp], 'exang': [exang], 'cp': [cp], 'chol': [chol], 'fbs': [bs], 'caa': [caa], 'thalachh': [max_hr]}
		dataFrame = pd.DataFrame(data)
		# make prediction
		result = model.predict(dataFrame)
		print(result) # log raw prediction from ml model to console

		# based on binary value from model, create a sentence
		if(result >= 0.5):
			output  = "High chance of heart attack"
		else:
			output = "Low chance of heart attack"

		print(output) # log result to the console
		return render_template('index.html', output=output)

	else:
		return render_template('index.html', output="")

web_site.run(host='0.0.0.0', port=8080)
