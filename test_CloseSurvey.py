import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/surveys/4c1a28ac-2e99-40e8-a314-563b33a31dfe"

payload = json.dumps({
  "isClosed": True
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}
def test_checkstatuscode():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  statuscode = response.status_code
  print(statuscode)
def test_fetchresponsebody():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_fetcherrorcode():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  errorcode = JsonObj['errors']
  print(errorcode)
  #assert errorcode == "error_access_denied"
def test_errorcodes():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  errcode=JsonObj['errors'][0]['msg']
  print(errcode)
  assert errcode == "error_must_not_yet_be_closed"







