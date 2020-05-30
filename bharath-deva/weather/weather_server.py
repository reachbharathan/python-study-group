from flask import Flask, render_template, request
import json
from urllib.request import urlopen 

app = Flask(__name__)
api_key = "eac7f9665ef2bdb0e603d3c9fc94c3b6"

def data_from_api(country):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={country["country"]}&appid={api_key}&units=metric'
    print(url)
    url_response = urlopen(url)
    weather_data = url_response.read()
    return weather_data

@app.route('/')
@app.route('/home')
def home():
    return render_template('weather_home.html')

@app.route('/submit_form',methods = ['POST'])
def submit():
    data = request.form.to_dict()
    weather_data = data_from_api(data)
    weather_data = weather_data.decode("utf-8")
    weather_data = json.loads(weather_data)
    return render_template('weather_submit.html', weather_data = weather_data)

