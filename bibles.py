import json

with open('available-bibles.json', 'r') as f:
    bibles_dict = json.load(f)

for bible in bibles_dict['data']:
    print(bible['id'] + '|' + bible['name'])

