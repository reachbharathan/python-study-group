from flask import Flask, render_template, request
# import json to load JSON data to a python dictionary
import json
# urllib.request to make a request to api
import urllib.request


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name mathura
        city = 'chennai'

    # your API key will come here
    api = "7fccc77ed9c1f1f56366a13535f46ddd"

    # source url
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
        city + '&appid=' + api + '&units=metric'
    print("Request city: ", city)
    print("Request URL: ", url)

    # source contain json data from api
    source = urllib.request.urlopen(url).read()

    # converting JSON data to a dictionary
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "city": city,
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
        + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + ' °C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
