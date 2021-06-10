# import all required packages
from flask import Flask, render_template, request
from random import choice
import tensorflow as tf
import keras
from keras.models import load_model
import pandas as pd

web_site = Flask(__name__)

model = load_model('model.h5') # load ML model

@web_site.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		data = {}
		dataFrame = pd.DataFrame(data)
		result = model.predict(dataFrame)
		if(result == 1):
			output  = "High chance of heart attack"
		else:
			output = "Low chance of heart attack"

		return render_template('index.html', output=output)

	else: 
		return render_template('index.html', output="")

web_site.run(host='0.0.0.0', port=8080)