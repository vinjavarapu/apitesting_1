import pprint

import requests
import json
from apitesting_1 import Config

url = "https://api.staging.artemis.im/projects/1311c8c1-456a-4194-ac1a-bd21e98dac2c"

payload = json.dumps({
  "isFavorite": True
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}
def test_checkstatuscode():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  statuscode=response.status_code
  print(statuscode)
  assert statuscode == 200
def test_verifyresponsebody():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_isFavoritefield_exists():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'isFavorite' in JsonObj['data']
def test_verifystatusof_IsFavorite():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  isFavorite = JsonObj['data']['isFavorite']
  print(isFavorite)
  assert isFavorite == True
def test_fetchProjectTitle():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  title_of_project = JsonObj['data']['title']
  print(title_of_project)



