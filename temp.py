import json

jsondata = json.loads(open('static/json/photos.json').read())
files = [photo['filename'] for photo in jsondata if photo['album'] == 'travel']
