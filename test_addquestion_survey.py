import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/surveys/386b4fd7-a178-476d-ab86-bc59585f4c02/questions"

payload = json.dumps({
  "text": "Selenium Question 1 ?",
  "modifiers": {},
  "type": "single_choice",
  "restrictions": {
    "choices": [
      "yes",
      "no"
    ]
  },
  "tags": [
    "general_health"
  ],
  "customTags": [],
  "ordinalNumber": 0
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

def test_statuscodeCheck():
  response = requests.request("POST", url, headers=headers, data=payload)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 200
def test_fetchResponseBody():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_verifyquestionTitle():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  title = JsonObj['data']['text']
  print("question title is", title)
def test_CheckQuestiontype():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  question_type = JsonObj['data']['type']
  print("Question type is ",question_type)
def test_fetchQuestionUUID():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  uuid_value = JsonObj['data']['uuid']
  print("UUID Value is ", uuid_value)
def test_skiplogicfieldexists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'skipLogic' in JsonObj['data']







