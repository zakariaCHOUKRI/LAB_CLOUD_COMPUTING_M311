import numpy as np
import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
target_names = joblib.load('target_names.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['sepal_length']),
        float(request.form['sepal_width']),
        float(request.form['petal_length']),
        float(request.form['petal_width'])
    ]
    
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)[0]
    prediction_text = f"Predicted Iris Class: {target_names[prediction]}"
    
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
