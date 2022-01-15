import pprint

import requests
import fileinput
import Config

url = "https://api.staging.artemis.im/media?type=project_banner"

payload={}

headers = {
  'Authorization': Config.token_user
}

def test_checkstatuscode():
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.status_code)
  assert response.status_code == 400
def test_checkResponseBody():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)




