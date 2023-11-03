import requests
import json

url = "https://dog.ceo/api/breeds/image/random"
response = json.loads(requests.request("GET", url).text)
print(response['message'])