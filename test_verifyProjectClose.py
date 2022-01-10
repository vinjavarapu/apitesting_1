import requests
import json
import Config

url = "https://api.staging.artemis.im/projects/68803e6d-073d-4706-ad2a-bb1c0b1940a8"

payload = json.dumps({
  "isClosed": True
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

def test_statuscode():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    statuscode = response.status_code
    print(statuscode)
    assert statuscode == 200
def test_verifyResponseBody():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    JsonObj = response.json()
    print(JsonObj)
def test_verifystatusofproject():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    JsonObj = response.json()
    statusofproject = JsonObj['status']
    print(statusofproject)


