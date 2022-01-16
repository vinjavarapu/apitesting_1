import requests
import json
from apitesting_1 import Config

url = "https://api.staging.artemis.im/surveys/0beafa67-9541-4d98-8d0a-2e6e2936310f"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_verifyStatusCode():
  response = requests.request("GET", url, headers=headers, data=payload)
  statuscode = response.status_code
  assert statuscode == 200
def test_retrievesurveyName():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  surveyName = JsonObj['data']['title']
  print(surveyName)
def test_retrivestatusofSurvey():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  status_of_survey = JsonObj['data']['status']
  print(status_of_survey)
def test_surveyCreatedDate():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  survey_createdDate = JsonObj['data']['createdAt']
  print(survey_createdDate)
def test_fetchUUID():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  survey_uuid = JsonObj['data']['uuid']
  print(survey_uuid)
  assert survey_uuid == "0beafa67-9541-4d98-8d0a-2e6e2936310f"






