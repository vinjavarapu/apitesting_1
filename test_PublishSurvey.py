import requests
import json
import Config

url = "https://api.staging.artemis.im/surveys/18e83321-3403-4d98-87e4-6b0823456aa6"

payload = json.dumps({
  "isPublished": True
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}
def test_statuscode():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  statuscode = response.status_code
  assert statuscode == 200
def test_fetchresponsebody():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  print(JsonObj)
def test_publishedstatus():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  status = JsonObj['data']['status']
  print('The status of survey is ',status)
  assert status == "published"
def test_publishedattimestamp():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  publishedat = JsonObj['data']['publishedAt']
  print(publishedat)
def test_titleofsurvey():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  title = JsonObj['data']['publishedAt']
  print(title)








