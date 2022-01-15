import pprint

import requests

url = "https://api.staging.artemis.im/goals/ping"

payload = ""
headers = {
  'Authorization': 'null'
}

def test_statuscheckcode():
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    assert response.status_code == 200
def test_fetchresponsebody():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    pprint.pprint(JsonObj)
def test_fetchdescription():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    description = JsonObj['description']
    print(description)
def test_fetchname():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    name = JsonObj['name']
    print(name)
def test_fetchdversion():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.json()
    version = JsonObj['version']
    print(version)




