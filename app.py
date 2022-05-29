
from pyexpat import features
from unittest import mock
import pandas as pd 
import numpy as np 
from flask import Flask,redirect, url_for,render_template ,request,jsonify
import pickle
app = Flask(__name__ )
model = pickle.load(open('model.pkl','rb'))
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict',methods=['post'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predicti = model.predict(final_features)
    output =  round(predicti[0],2)
    return render_template("index.html",prediction="Employer salary should be $ {} ".format(output))

if __name__ == '__main__':
    app.run(debug=True )
    
    
    