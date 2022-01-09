import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/projects/ebd83f2b-cc17-4d16-9d0e-93e1bcc97dde"

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



