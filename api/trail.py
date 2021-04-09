import requests, json

data = requests.get('http://127.0.0.1:8000/player_info/')
attack_data = requests.get('http://127.0.0.1:8000/player_attacking_stats/')

x = data.json()
ax = attack_data.json()
names = []
attak_names = []
for item in x:
    names.append(item["name"])

for item in ax:
    attak_names.append(item["name"])

print(names)
print(attak_names)