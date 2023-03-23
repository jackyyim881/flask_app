# import requests
# r =  requests.get("https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=flw&lang=tc")
# r.encoding = "utf-8"
# print(r.text)




from flask import Blueprint

bp = Blueprint('api', __name__)



from app.api import routes




# r2 = requests.get('http://httpbin.org/get', params=data)

# print(r2.text)

# r = requests.get('http://httpbin.org/get')

# data = {
#     'name': state,
# }
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
    
#     # print(manual_added)

#     return data

# r = requests.get('http://httpbin.org/get', params=validate_record_schema(record.json()))
# print(r.text)