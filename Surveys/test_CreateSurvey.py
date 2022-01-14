import pprint
import requests
import json
import Config

url = "https://api.staging.artemis.im/surveys"

payload = json.dumps({
  "projectUuid": "cd5bdcc4-7bd8-4e7e-ae0c-b60846ced145"
})


headers = {
  'Authorization':Config.token_user,
  'Content-Type': 'application/json'
}



def test_statuscodeof_CreateSurveyAPICall():
  response = requests.request("POST", url, headers=headers, data=payload)
  response_body = response.json()
  statuscode = response.status_code
  assert statuscode == 201
def test_fetchtheURLofSurvey():
  response = requests.request("POST", url, headers=headers, data=payload)
  surveyurl = response.url
  print(surveyurl)

def test_fetchtheResponseBody():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_RetriveUUIDofSurvey():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  uuid_value = JsonObj['data']['uuid']
  print(uuid_value)
def test_Verifystatusfield_exists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'status' in JsonObj['data']
def test_VerifyTitleOfSurvey_exists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'title' in JsonObj['data']
def test_VerifyCreatedAtfield_exists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'createdAt' in JsonObj['data']

def test_VerifyUpdatedAtfield_exists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'updatedAt' in JsonObj['data']








