import requests
import json
import Config

url = "https://api.staging.artemis.im/projects/68803e6d-073d-4706-ad2a-bb1c0b1940a8"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_statuscode():
    response = requests.request("DELETE", url, headers=headers, data=payload)
    statuscode = response.status_code
    print(statuscode)
    print(response.text)
def test_error_project_does_not_exist():
    response = requests.request("DELETE", url, headers=headers, data=payload)
    JsonObj = response.json()
    err_code = JsonObj['errors'][0]['msg']
    assert err_code == "error_project_does_not_exist"






