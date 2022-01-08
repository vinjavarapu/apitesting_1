import requests
import json
import Config

url = "https://api.staging.artemis.im/surveys/6aea9222-a6e2-41c4-8513-6baffdab410f"

payload = json.dumps({
  "title": "Updated survey title"
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

def test_statuscode():

  response = requests.request("PATCH", url, headers=headers, data=payload)
  statuscode=response.status_code
  print(statuscode)
  assert statuscode == 200

def test_fetchtheresponsebody():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  print(JsonObj)

def test_questionsfieldPresent():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  assert 'questions' in JsonObj['data']

def test_TitleProject():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  title = JsonObj['data']['project']['title']
  print('The title of project  is ', title)

def test_updatedSurveyTitle():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  surveyname = JsonObj['data']['title']
  print(surveyname)







