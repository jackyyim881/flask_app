from flask import render_template, flash, redirect, url_for, request, g, session
from app.api import bp
import requests ,json

record = requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc")
record.encoding = "utf-8"


def validate_record_schema(record):
    # manual_added  = record.get('weatherForecast')[1].get('forecastMintemp')
    latest_forecast = record.get('weatherForecast')[0]
    manual_added  = record.get('weatherForecast')[1].get('forecastMintemp')

    data = {
        'weatherForecast': manual_added.get('value'),
        'forecastMintemp': manual_added.get('unit'),
        "forecastDate": latest_forecast.get('forecastDate'),
        "week": latest_forecast.get('week'),
        "forecastMaxtemp": latest_forecast.get('forecastMaxtemp').get('value'),
    }

    # print(manual_added)

    return data

r = requests.get('http://httpbin.org/get', params=validate_record_schema(record.json()))
print(r.text)

@bp.route('/weather1')
def query_example():
    record = requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc")
    r = requests.get('http://httpbin.org/get', params=validate_record_schema(record.json()))
    # if key doesn't exist, returns None
    # print(r.json().get('args').get('key'))
    args = r.json().get('args')

    return render_template('weather/weather1.html', query = r.text , args = args)
    # print(manual_added)




    
    # print(manual_added)


# r = requests.get('http://httpbin.org/get', params=validate_record_schema(record.json()))
# print(r.text)
# record = requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc")
# record.encoding = "utf-8"
# def validate_record_schema(record):
#     # manual_added  = record.get('weatherForecast')[1].get('forecastMintemp')
#     latest_forecast = record.get('weatherForecast')[0]
#     manual_added  = record.get('weatherForecast')[1].get('forecastMintemp')

#     data = {
#         'weatherForecast': manual_added.get('value'),
#         'forecastMintemp': manual_added.get('unit'),
#         "forecastDate": latest_forecast.get('forecastDate'),
#         "week": latest_forecast.get('week'),
#         "forecastMaxtemp": latest_forecast.get('forecastMaxtemp').get('value'),
#     }