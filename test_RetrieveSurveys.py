import pprint
import Config
import requests

url = "https://api.staging.artemis.im/surveys?projectUuid=79683bf6-982a-452a-a644-ffa4aa92864b"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_checkStatusCode():
  response = requests.request("GET", url, headers=headers, data=payload)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 200
def test_RetrieveResponseBody():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_totalnoofsurveys():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print("The total number of records are ",JsonObj['pagination']['total'])







