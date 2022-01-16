import pprint

import requests
import json

from apitesting_1 import Config

url = "https://api.staging.artemis.im/actions"

payload={}
headers = {
  'Authorization': Config.token_user
}

def test_checkstatuscode():
  response = requests.request("GET", url, headers=headers, data=payload)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 200
def test_fetchresponsebody():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_fetchmessage():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  message = JsonObj['message']
  print(message)
  assert message == "retrieve all action successful"





