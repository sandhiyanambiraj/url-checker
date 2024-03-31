from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np

from API import get_prediction
app = Flask(__name__)

# Load the trained model
model = '../Phishing-Attack-Domain-Detection/models/Malicious_URL_Prediction.h5'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        prediction = get_prediction(url,model)
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
