import requests
import json

# API endpoint - this might need to be modified based on what data you need
url = "https://clinicaltrials.gov/api/v2/studies"

# Make a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()
    # Do something with the data
    print(data)
else:
    print("Failed to retrieve data: Status code", response.status_code)
