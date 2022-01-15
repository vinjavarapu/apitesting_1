import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/dashboards"

payload = json.dumps({
  "name": "new dashboard test for Favorites",
  "description": "just a random dashboard description"
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

def test_statuccheckcode():
  response = requests.request("POST", url, headers=headers, data=payload)
  statuscode = response.status_code
  assert statuscode == 201
def test_fetchResponsebody():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_verifyname():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  name = JsonObj['data']['name']
  print("The title of dashboard is" , name)
def test_dashbiardcreatedby():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  CreatedBy = JsonObj['data']['createdBy']
  print(CreatedBy)
def test_dashboarddescription():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  description = JsonObj['data']['description']
  print(description)










