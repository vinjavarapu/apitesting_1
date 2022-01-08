import requests

url = "https://api.staging.artemis.im/surveys/4c1a28ac-2e99-40e8-a314-563b33a31dfe"

payload = ""
headers = {
  'Authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjFkMmE2YTZhNDcyYWNhNjNmM2FmNzU2NjIxZjM0Njg2OTI1YjUxYTgiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiUmF2aStWaW5qYXZhcmFwdSIsInBpY3R1cmUiOiJodHRwczovL21lZGlhLnN0YWdpbmcuYXJ0ZW1pcy5pbS91c2Vycy9jZWFiMWRiYS1hZjJmLTQyYjUtYWQ4MC01MzlkMWMxOTE1NDYvcHJvZmlsZS1waG90b3MvY2Y2MTcyY2EtOThhYy00N2NmLTgxODYtNTI0YjI5YTZiNDU4LmpwZWciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYXJ0ZW1pcy1zdGFnaW5nLTUxNTAyIiwiYXVkIjoiYXJ0ZW1pcy1zdGFnaW5nLTUxNTAyIiwiYXV0aF90aW1lIjoxNjQwOTM0OTIxLCJ1c2VyX2lkIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsInN1YiI6ImZRelhqSlp0dlJXcW04aWRKQnR3dktHRDgzYzIiLCJpYXQiOjE2NDA5MzQ5MjEsImV4cCI6MTY0MDkzODUyMSwiZW1haWwiOiJ2aW5qYXZhcmFwdUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMDgwMTg1NTg5ODgyMjIwMjA2MiJdLCJlbWFpbCI6WyJ2aW5qYXZhcmFwdUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.UZzWggosazIERnWhNEZfb8Pk_2AkIWqoETXNVtiLrmhra24UfNQ0osRA-kOAveVlR8A0BFDV4c05L6utTrxWD12AB-ev84NQqWWQvrtKBF-Dm6oYq3kdtsjjHwQ0alMvF2opffqDEM-Omzicz1_FGHM0qUB_73UpePEqNtq-sxgzvXCau7cr86pJH8N83rasX8Lf7QwkvrbgQSHA6Rx7KltPV0QEAnlA1h0Qbbqpq-quC8pj1TxJ_6JJdvhQ-gRY8tM308f578Ui2-aLtMCpmLWVnp5G0jDrmeeQg7Ny3EwGQf11TU6DRWU32gjwdgO0-dIyWhpmAvQNYGISCLm-7g'
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
  assert survey_uuid == "4c1a28ac-2e99-40e8-a314-563b33a31dfe"






