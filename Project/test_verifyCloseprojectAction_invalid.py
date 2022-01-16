import requests
import json
from apitesting_1 import Config

url = "https://api.staging.artemis.im/projects/c96f9de1-4919-45d6-b09d-c6215dfc5aa6"

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
    assert statuscode == 400
def test_fetchresponsebody():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    JsonBody = response.json()
    print(JsonBody)
def test_fetcherrormessage():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    JsonBody = response.json()
    errormessage = JsonBody['message']
    print(errormessage)
    assert errormessage == "Failed to validate request"
def test_verify_error_access_denied():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    JsonBody = response.json()
    errorcode = JsonBody['errors'][0]['msg']
    print(errorcode)
    assert errorcode == "error_access_denied"
def test_verify_error_project_not_yet_published():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    JsonBody = response.json()
    errorcode = JsonBody['errors'][1]['msg']
    print(errorcode)
    assert errorcode == "error_project_not_yet_published"





