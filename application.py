from flask import Flask, render_template, request
import pickle
import numpy as np

from src.pipeline.predict_pipeline import CustomData, PredictionPipeline

model = pickle.load(open('artifacts/model.pkl', 'rb'))

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    dayOfMonth = int(request.form.get('day_of_month'))
    dayOfWeek = int(request.form.get('day_of_week'))
    month = int(request.form.get('month'))
    precipitation = float(request.form.get('precipitation'))
    windSpeed = float(request.form.get('wind_speed'))
    humidity = int(request.form.get('humidity'))
    hour = int(request.form.get('hour'))
    temperature = float(request.form.get('temperature'))

    data = CustomData(hour, temperature, humidity, windSpeed, month, dayOfMonth, dayOfWeek, precipitation).getDataArr()
    result = PredictionPipeline().predict(data)

    res = f'Predicted Bike Demand: {result}'
    return render_template('index.html', result=res)

if __name__ == '__main__':
    app.run()