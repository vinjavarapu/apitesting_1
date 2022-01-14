import requests

import Config

url = "https://api.staging.artemis.im/users/ceab1dba-af2f-42b5-ad80-539d1c191546"

payload = ""
headers = {
  'Authorization': Config.token_user
}

def test_statuscheckcode():
  response = requests.request("GET", url, headers=headers, data=payload)
  print(response.status_code)
def test_checkresponsebody():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print(JsonObj)
def test_checkprojectsCreated():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  projectsCreated = JsonObj['result']['projectsCreated']
  print("The user created the number of project is equal to " , "" , projectsCreated)

def test_checksubscriptionofuser():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  subscriptionBillingPeriod = JsonObj['result']['subscriptionBillingPeriod']
  print("The user subscription ", "",subscriptionBillingPeriod )
def test_checkSurveysCreated():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  surveysAnswered = JsonObj['result']['surveysAnswered']
  print("The user created the number of project is equal to " , "" , surveysAnswered)








