import requests

# Specify the API endpoint URL and data to send
id=123
api_url = "http://127.0.0.1:8000/api/items_update/4"  # Replace with the actual API endpoint URL
data = {
    "name": "ilam",
    "population": "458000",
    
}

# Make a PUT request to the API
response = requests.put(api_url, json=data)

# Check if the request was successful (status code 200 or 204)
if response.status_code in (200, 204):
    print("PUT Request Successful")
else:
    print("PUT Request Failed with status code:", response.status_code)