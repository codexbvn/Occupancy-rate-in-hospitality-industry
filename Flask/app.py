from flask import Flask,render_template,request
from datetime import datetime
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app=Flask(__name__) #Creates an instance of web application
#@ is the decorators

import pickle
model=pickle.load(open(r'D:/Externship/Flask/model.pkl','rb'))

@app.route('/') #Route is used to redirect the user to a specific page. This single slash represents home page. 
def hello_world():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def predict():
    p=request.form["date"]
    q=float(request.form["temperature"])
    r=float(request.form["humidity"])
    s=float(request.form["light"])
    t=float(request.form["co2-input"])
    u=float(request.form["humidity-ratio"])
    datetime_obj = datetime.strptime(p, '%Y-%m-%dT%H:%M')
    day_name = datetime_obj.strftime('%A')
    hour = datetime_obj.strftime('%H')
    data={'temperature': [q], 'humidity': [r], 'light': [s], 'co2-input': [t], 'humidity-ratio': [u],'day':[day_name],'hour':[hour]}
    df = pd.DataFrame(data)
    day_mapping = {'Monday': 1, 'Tuesday': 5, 'Wednesday': 6, 'Thursday': 4, 'Friday': 0, 'Saturday': 2, 'Sunday': 3}
    df['day'] = df['day'].map(day_mapping)
    scale=MinMaxScaler()
    column_names1 = df.columns
    scaled_x_train=pd.DataFrame(scale.fit_transform(df),columns=column_names1)
    output=model.predict(scaled_x_train)
    prediction = "Unavailable" if output == 1 else "Available"

    return render_template("index.html",y="The predicted availability is "+ prediction)
    

if __name__=='__main__':
    app.run(debug=False)
    #if debug is False you can't do any modifications while it is running.
