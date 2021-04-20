import requests, json

data = requests.get('http://127.0.0.1:8000/api/player_info/')

x = data.json()


print(x)