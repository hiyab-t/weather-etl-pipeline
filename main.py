import requests


#define the API endpoint

api_url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 51.5074,
    "longitude": -0.1278,
    "hourly": "temperature_2m"
}

#make a GET request to fetch data
response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully!")
else: 
    print("Failed to fetch data:", response.status_code)