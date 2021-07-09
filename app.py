#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import the required libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ''' This will predict the species of the flower'''
    int_convert = [float(x) for x in request.form.values()]
    features = [np.array(int_convert)]
    prediction = model.predict(features)
    prediction_str = np.array_str(prediction)
    final_str = prediction_str.strip("][''")
    
    return render_template('index.html', prediction_text='The predicted species flower is {}'.format(final_str))

if __name__ == "__main__":
    app.run(debug=True)

