import requests
import parameters

bible_id = parameters.BIBLE_ID
url = 'https://api.scripture.api.bible/v1/bibles/' + bible_id + '/books'

headers = {'api-key': parameters.API_KEY}
r = requests.get(url, headers=headers)

print(r.text)
