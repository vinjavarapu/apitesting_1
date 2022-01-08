import pprint
import requests
import json
import Config

url = "https://api.staging.artemis.im/surveys"

payload = json.dumps({
  "projectUuid": "ebd83f2b-cc17-4d16-9d0e-93e1bcc97dde"
})
headers = {
  'Authorization':Config.token_user,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


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








