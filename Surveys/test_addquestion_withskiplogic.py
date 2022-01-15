import pprint

import requests
import json
import Config

url = "https://api.staging.artemis.im/surveys/a10407b7-d411-4ede-b0cd-04240cedec7f/questions"

payload = json.dumps({
  "text": "SkipLogicWith",
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
  "ordinalNumber": 0,
  "skipLogic": [
    {
      "answer": "no",
      "skipTo": 5
    }
  ]
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

def test_statuscode():
  response = requests.request("POST", url, headers=headers, data=payload)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 200
def test_Fetchtheresponsebody():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
def test_verifySkiplogicfieldexists():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'skipLogic' in JsonObj['data']
def test_skiplogicdata():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  skiplogic_data = JsonObj['data']['skipLogic']
  pprint.pprint(skiplogic_data)
def test_skipLogicanswer():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  skiplogic_data = JsonObj['data']['skipLogic']
  answer = skiplogic_data[0]
  print(answer)
def test_questiontitle():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  title = JsonObj['data']['text']
  print("The question title is ", title)
def test_verifyMandatoryquestion():
  response = requests.request("POST", url, headers=headers, data=payload)
  JsonObj = response.json()
  isrquired = JsonObj['data']['isRequired']
  print(isrquired)
  assert isrquired ==  True









