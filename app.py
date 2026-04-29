from flask import Flask, render_template, request
from datetime import datetime
import pandas as pd
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model  = pickle.load(open(os.path.join(BASE_DIR, 'model.pkl'),  'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'scaler.pkl'), 'rb'))
le     = pickle.load(open(os.path.join(BASE_DIR, 'le.pkl'),     'rb'))

# Feature columns must match training order exactly
FEATS = ['Temperature','Humidity','Light','CO2','HumidityRatio','day','hour']


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    status = None

    if request.method == 'POST':
        try:
            date_str  = request.form['date']
            temp      = float(request.form['temperature'])
            humidity  = float(request.form['humidity'])
            light     = float(request.form['light'])
            co2       = float(request.form['co2'])
            hum_ratio = float(request.form['humidity_ratio'])

            dt       = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
            day_name = dt.strftime('%A')              # e.g. 'Wednesday'
            day_enc  = le.transform([day_name])[0]   # same LabelEncoder as training
            hour_val = dt.hour

            row = pd.DataFrame([{
                'Temperature':    temp,
                'Humidity':       humidity,
                'Light':          light,
                'CO2':            co2,
                'HumidityRatio':  hum_ratio,
                'day':            day_enc,
                'hour':           hour_val,
            }], columns=FEATS)

            row_scaled = pd.DataFrame(scaler.transform(row), columns=FEATS)
            pred = model.predict(row_scaled)[0]

            if pred == 1:
                result = "Room is currently Occupied"
                status = "occupied"
            else:
                result = "Room is Available"
                status = "available"

        except Exception as e:
            result = f"Prediction error — {e}"
            status = "error"

    return render_template('index.html', result=result, status=status)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
