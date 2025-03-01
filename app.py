from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Load models and encoders
model = pickle.load(open('LGBM_model.pkl', 'rb'))
oe = pickle.load(open('ordinal_encoder.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    # Extract input values from the form
    Brand = float(request.form['Brand'])
    Material = float(request.form['Material'])
    Size = float(request.form['Size'])
    Compartments = float(request.form['Compartments'])
    Laptop_Compartment = float(request.form['Laptop_Compartment'])
    Waterproof = float(request.form['Waterproof'])
    Style = float(request.form['Style'])
    Color = float(request.form['Color'])
    Weight_Capacity_kg = float(request.form['Weight_Capacity_kg'])  # Convert numeric input

    # Create feature list
    #feature_list = [[Brand, Material, Size, Compartments, Laptop_Compartment, Waterproof, Style, Color, Weight_Capacity_kg]]
    # Encode categorical features
    #feature_array = oe.transform(feature_list)  # Transform using ordinal encoder

    def recommendation(Brand, Material, Size, Compartments, Laptop_Compartment, Waterproof, Style, Color, Weight_Capacity_kg):
        features = np.array([[Brand, Material, Size, Compartments, Laptop_Compartment, Waterproof, Style, Color, Weight_Capacity_kg]])
        prediction = model.predict(features).reshape(1,-1)
        return prediction[0]

    # Predict price
    #prediction = model.predict(feature_array)
    predict= recommendation(Brand, Material, Size, Compartments, Laptop_Compartment, Waterproof, Style, Color, Weight_Capacity_kg)

    # Prepare result message
    #predicted_price = round(prediction[0], 2)  # Ensure it's a readable format
    result = f"{predict}"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
