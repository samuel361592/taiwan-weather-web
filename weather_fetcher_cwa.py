import requests

API_KEY = "CWA-DFBA99C7-B637-4C30-B675-4407927C637C"
API_URL = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

def fetch_weather(city):
    params = {
        "Authorization": API_KEY,
        "format": "JSON"
    }

    res = requests.get(API_URL, params=params)
    data = res.json()

    if "records" not in data or "location" not in data["records"]:
        return []

    locations = data["records"]["location"]

    for location in locations:
        if location["locationName"] == city:
            elements = location["weatherElement"]
            wx = elements[0]["time"]
            min_temp = elements[2]["time"]
            max_temp = elements[4]["time"]

            forecast = []
            for i in range(len(wx)):
                forecast.append({
                    "start": wx[i]["startTime"],
                    "end": wx[i]["endTime"],
                    "weather": wx[i]["parameter"]["parameterName"],
                    "min": min_temp[i]["parameter"]["parameterName"],
                    "max": max_temp[i]["parameter"]["parameterName"]
                })
            return forecast

    return []
