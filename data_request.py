import requests

url = "https://api.opensea.io/api/v1/collections?offset=0&limit=300"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
