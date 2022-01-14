import pprint

import requests
import json

import Config

url = "https://api.staging.artemis.im/users/_me"

Update_User = open("UpdateUser.json","r").read()
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}
def test_checkstatuscode():
  response = requests.request("PATCH", url, headers=headers, data=Update_User)
  print(response.status_code)
def test_retrieveresponsebody():
  response = requests.request("PATCH", url, headers=headers, data=Update_User)
  JsonObj = response.json()
  pprint.pprint(JsonObj)





