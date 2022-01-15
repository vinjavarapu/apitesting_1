import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/categories/ping"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_checkstatuscode():
  response = requests.request("GET", url, headers=headers, data=payload)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 200
def test_fetchtheresponsebody():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_descriptioncontentdisplay():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  description = JsonObj['description']
  print(description)
def test_versioninfo():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  version_info = JsonObj['version']
  print(version_info)








