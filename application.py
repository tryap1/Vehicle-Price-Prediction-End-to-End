import requests
from flask import Flask, render_template, request
import jsonify
import numpy as np
import sklearn
import pickle

model = pickle.load(open('RandomForestRegressor.pkl', 'rb'))


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    
    if request.method == "POST":
        age = int(request.form['age'])
        price = float(request.form['price'])
        km = int(request.form['km'])
        owners = int(request.form['owners'])
        fuel = request.form['fuel_type']
        if fuel == 'Petrol':
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        elif fuel == 'Diesel':
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
        seller = request.form['seller']
        if seller == 'Individual':
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        transmission = request.form['transmission']
        if transmission == "Automatic":
            Transmission_Mannual=0
        else:
            Transmission_Mannual=1
            
        prediction = model.predict([[price,km,owners,age,Fuel_Type_Diesel, Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])    
        prediction = np.round(prediction, 2)
        return render_template('index.html', prediction_text = "Estimated Sale Value: {} in Lahks".format(prediction))
    
    else:
        return render_template('index.html')
    
    
if __name__=="__main__":
    app.run(debug=True)    

