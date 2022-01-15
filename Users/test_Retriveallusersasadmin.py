import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/users/?origin=admin"

payload = ""
headers = {
  'Authorization': Config.token_admin
}

def test_checkstatuscode():
  response = requests.request("GET", url, headers=headers, data=payload)
  statuscode = response.status_code
  assert statuscode == 200 , "Please update the admin token "
def test_fetchresponsebody():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_fetchtotalnoofusers():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  total_users = JsonObj['pagination']['total']
  print("The total number of users are " , total_users)




