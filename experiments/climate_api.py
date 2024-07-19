import requests

# Define the API URL
url = 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=Y952srczIVewZdzqIEzVhG9lKBdmeVsP'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print the raw JSON data
    print(data)
    
    # Example: Extract specific information (e.g., current temperature)
    current_weather = data.get('data', {}).get('current', {})
    temperature = current_weather.get('temperature', 'No data available')

    print(f"Current Temperature: {temperature}°C")
else:
    print(f"Error: {response.status_code}")
