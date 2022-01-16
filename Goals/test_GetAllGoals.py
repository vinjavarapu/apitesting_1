import requests
import json
from apitesting_1 import Config

url = "https://api.staging.artemis.im/goals"

payload={}
headers = {
  'Authorization': Config.token_user
}

def test_statuscheckcode():
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    assert response.status_code == 200
def test_retrieveresponsebody():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    print(JsonObj)
    Goalkey = JsonObj['result'][0]['subgoals'][0]['key']
    print(Goalkey)
    assert Goalkey == "SDG_1_1"
def test_retrieveuuid():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    print(JsonObj)
    uuid = JsonObj['result'][0]['subgoals'][0]['uuid']
    print(uuid)






