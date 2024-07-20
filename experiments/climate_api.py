import pandas as pd
import json

# Load JSON data from file
with open(r'C:\Users\Keyur Mistry\Desktop\Agri_project\data\weather_data.json', 'r') as file:
    data = json.load(file)

# Convert JSON data to DataFrame
df = pd.json_normalize(data)

# Save DataFrame to CSV file
df.to_csv('path_to_your_output_file.csv', index=False)
