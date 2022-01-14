import requests
import json
import Config

url = "https://api.staging.artemis.im/projects/ee414410-a40f-4e52-977f-0768c93926ba"

payload = json.dumps({
  "title": "Project API Change Goal 3",
  "goalUuid": "b3e1af0a-367e-4887-bbcc-38dcfc9e7eea",
  "subgoalUuid": "3e48bbc2-2c8d-4548-a9cf-6a47ed61c175"
})
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
def test_statucCodeis200():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  print(response.text)
  assert response.status_code == 400

def test_FetchtheresponseBody():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  print(JsonObj)
def test_errormessagedetails():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  err_msg = JsonObj['message']
  assert err_msg == "Failed to validate request"

def test_fetchtheerrorcodes():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  err_code = JsonObj['errors'][0]['msg']
  print(err_code)
  assert err_code == "error_project_does_not_exist"

def test_fetchaccessdeniederrormsg():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  err_code = JsonObj['errors'][1]['msg']
  print(err_code)
  assert err_code == "error_access_denied"
def test_fetcherrorGoaldoesnotexists():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  err_code = JsonObj['errors'][2]['msg']
  print(err_code)
  assert err_code == "error_goal_does_not_exist"
def test_fetcherrorSUBGoaldoesnotexists():
    response = requests.request("PATCH", url, headers=headers, data=payload)
    JsonObj = response.json()
    err_code = JsonObj['errors'][3]['msg']
    print(err_code)
    assert err_code == "error_subgoal_does_not_exist"








