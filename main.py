from utils import config
from connect import *
import pprint
from urllib.parse import urlencode
import requests

import json


uri = f'https://api.aviationstack.com/v1/flights?access_key={config['FAA_API_KEY']}'

response = requests.get(uri)
q = {

}
res = response.json()

with open('response.json', 'w') as f:
  f.write(json.dumps(res))

