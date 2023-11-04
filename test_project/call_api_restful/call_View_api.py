import requests

api_url='http://127.0.0.1:8000/api/items'
response=requests.get(api_url)
if response.status_code == 200:
    data=response.json()
    print('API Response :',data)
else:
    print('Api response failed:',response.status_code)
    