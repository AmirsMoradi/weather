import requests

# api key
api_key = "24418a6f48cb591c1ed31b5887bfc4c6"

# api address
url = f"http://api.openweathermap.org/data/2.5/weather?q=Tehran,IR&appid={api_key}&units=metric"

#send response api
response = requests.get(url)

# invert to JSON
data = response.json()
#weather information
if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print(f"Error fetching data: {response.status_code}")