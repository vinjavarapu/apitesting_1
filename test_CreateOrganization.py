import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/users/_me/organizations"

payload = json.dumps({
  "displayName": "Venkateswara1"
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

#test_json = open("Create_Organization.json","r").read()

def test_checkstatuscode():
  response = requests.request("POST", url, headers=headers, data=payload)
  statuscode = response.status_code
  assert statuscode == 201
def test_fetchresponsebody():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_actualSubscriptionTier_fieldexists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'actualSubscriptionTier' in JsonObj['data']
def test_fetchactualSubscriptionTier():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  actualSubscriptionTier_Value = JsonObj['data']['actualSubscriptionTier']
  print(actualSubscriptionTier_Value)
  assert actualSubscriptionTier_Value == "free"
def test_verifyDisplayNamefield_exists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'displayName' in JsonObj['data']
def test_fetchaOrgName():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  OrgName = JsonObj['data']['displayName']
  print(OrgName)
  assert OrgName == "Venkateswara1"
def test_excessSeatingfield_exists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'excessSeating' in JsonObj['data']











