import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/projects/43879449-6ecc-402f-8fa4-fab77c4ddc9a"

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
  assert statuscode == 400
def test_fetchresponseBody():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonBody = response.json()
  pprint.pprint(JsonBody)
def test_fetcherrormessage():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonBody = response.json()
  errormessage = JsonBody['errors'][0]['msg']
  print(errormessage)
  assert errormessage == "error_project_does_not_exist"
def test_responsebodyerrormessage():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonBody = response.json()
  errormessage = JsonBody['message']
  print(errormessage)
  assert errormessage == "Failed to validate request"
def test_error_access_denied():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonBody = response.json()
  errormessage = JsonBody['errors'][1]['msg']
  print(errormessage)
  assert errormessage == "error_access_denied"








