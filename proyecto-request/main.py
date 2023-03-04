import requests

URL = 'https://randomuser.me/api/'

response = requests.get(URL)

if response.status_code == 200:
  print(response.json())