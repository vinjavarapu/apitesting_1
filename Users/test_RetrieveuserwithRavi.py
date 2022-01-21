import pprint

import requests
from apitesting_1 import Config
import json



url = "https://api.staging.artemis.im/users/?query=Ravi"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_statuscheckcode():
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    assert response.status_code == 200
def test_fetchresponsebody():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    pprint.pprint(JsonObj)
def test_fetchdisplayName():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    displayName = JsonObj['data'][0]['displayName']
    print(displayName)
def test_fetchemailoffirstrecord():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    email = JsonObj['data'][0]['email']
    print(email)
def test_fetchUUID():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    uuid = JsonObj['data'][0]['uuid']
    print(uuid)
    assert uuid == "3ce47ca6-1668-4bfa-bb51-ca3d8a778608"








