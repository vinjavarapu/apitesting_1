import requests
import json
from apitesting_1 import Config

url = "https://api.staging.artemis.im/categories"

payload={}
headers = {
  'Authorization': Config.token_user
}

def test_statuscheckcode():
  response = requests.request("GET", url, headers=headers, data=payload)
  statuscode = response.status_code
  print(response.text)
  print(statuscode)
  assert statuscode == 200
def test_retrivesuccesfulmessage():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  message = JsonObj['message']
  print(message)
  assert message == "retrieve all categories successful"
def test_fetchnameofcategory():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  nameofcategory = JsonObj['result'][0]['name']
  print(nameofcategory)
  assert nameofcategory == "Child and Youth Development"
def test_fetchuuidofcategory():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  uuid_category = JsonObj['result'][0]['uuid']
  print(uuid_category)
  assert uuid_category == "c8cca1c1-49d1-441c-9998-ad657a16184f"
def test_fetchkeyofcategory():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  key_category = JsonObj['result'][0]['key']
  print(key_category)
  assert key_category == "CTG_YOUTH"
def test_verifynumberofcategories():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print(len(JsonObj['result']))








