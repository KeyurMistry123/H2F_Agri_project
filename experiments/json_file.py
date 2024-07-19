import requests
import json

# Define the API URL
url = 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=Y952srczIVewZdzqIEzVhG9lKBdmeVsP'

# Make the API request
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Save the JSON data to a file
    with open('weather_data.json', 'w') as file:
        json.dump(data, file, indent=4)  # `indent=4` makes the JSON file readable

    print("Data saved to weather_data.json")
else:
    print(f"Error: {response.status_code}")
