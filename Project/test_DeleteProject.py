import requests
import json
from apitesting_1 import Config

url = "https://api.staging.artemis.im/projects/c62eaa0b-7886-4068-aa12-a93e5ec9e07a"

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






