import requests
API_KEY = "5b08b1fb6c8c4db5b8881949252810"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
# Specify the city you want weather for
city = "Addis Ababa"

# Make the API request
response = requests.get(f"{BASE_URL}?key={API_KEY}&q={city}")

# Check if the request was successful
# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    weather_data = response.json()
    
    # Extract relevant weather information
    location = weather_data['location']['name']
    country = weather_data['location']['country']
    temperature = weather_data['current']['temp_c']
    weather_desc = weather_data['current']['condition']['text']
    
    # Print the weather information
    print(f"Weather in {location}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_desc}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
