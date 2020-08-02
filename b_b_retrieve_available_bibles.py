import requests
import a_a_parameters_connection as pc
import b_a_parameters_bibles as pbs
import json
from tinydb import TinyDB, Query


url = pc.BASE_API_URL + '/v1/bibles?language=' + pbs.LANGUAGE

headers = {'api-key': pc.API_KEY}
r = requests.get(url, headers=headers)

bibles_dict = json.loads(r.text)

db = TinyDB('b_c_db_bibles_'+pbs.LANGUAGE+'.json')
db.truncate()

for bible in bibles_dict['data']:
    db.insert(bible)

print(len(db))


