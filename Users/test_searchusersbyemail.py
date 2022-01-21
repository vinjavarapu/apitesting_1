import pprint

import requests
import json
from apitesting_1 import Config

url = "https://api.staging.artemis.im/users?query=%2B639160000001"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_statuscheckcode():
    response = requests.request("GET", url, headers=headers, data=payload)
    statuscode = response.status_code
    assert statuscode == 200
def test_checkresponsebody():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    pprint.pprint(JsonObj)
def test_verifydisplayName():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    displayName = JsonObj['data'][0]['displayName']
    pprint.pprint(displayName)
    assert displayName == "Tester21"
def test_fetchPhoneNumber():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    phoneNumber = JsonObj['data'][0]['phoneNumber']
    pprint.pprint(phoneNumber)
def test_verifyscoreofuser():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    score = JsonObj['data'][0]['score']
    pprint.pprint(score)
def test_isSubscriptionExpired():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    isSubscriptionExpired = JsonObj['data'][0]['isSubscriptionExpired']
    pprint.pprint(isSubscriptionExpired)
def test_photoURL_exists():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    photoURL = JsonObj['data'][0]['photoURL']
    pprint.pprint(photoURL)







