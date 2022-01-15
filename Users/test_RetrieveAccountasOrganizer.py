import pprint

import requests
import Config
import json

url = "https://api.staging.artemis.im/users/ceab1dba-af2f-42b5-ad80-539d1c191546?origin=organizer"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_statuscheckcode():
  response = requests.request("GET", url, headers=headers, data=payload)
  print(response.status_code)
  assert response.status_code == 200, "The token is not valid, please update the token value"
def test_fetchresponsebody():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_actualSubscriptionTier_Value():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  actualSubscriptionTier = JsonObj['result']['actualSubscriptionTier']
  print(actualSubscriptionTier)
  assert actualSubscriptionTier == "starter", "The token is not valid, please refresh the account"
def test_fetchDisplayName():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  displayName = JsonObj['result']['displayName']
  print(displayName)
  assert displayName == "Ravi Vinjavarapu", "The token is not valid, please refresh the account"
def test_fetchuseremail():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  email = JsonObj['result']['email']
  print(email)
  assert email == "vinjavarapu@gmail.com", "The token is not valid, please refresh the account"
def test_emailVerified():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  emailVerified = JsonObj['result']['emailVerified']
  print(emailVerified)
  assert emailVerified == True, "The token is not valid, please refresh the account"
def test_AccountCreatedTime():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  createdAt = JsonObj['result']['createdAt']
  print(createdAt)
  assert createdAt == "2021-11-26T06:22:35.120Z"












