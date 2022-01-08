import requests
import json

url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBL-odvK_jvqVc5la-PjXVEOc0j25dAfxk"

payload_emptyemail = json.dumps({
  "email": "",
  "password": "Ravi@123",
  "returnSecureToken": "true"
})
payload_emptypassword = json.dumps({
  "email": "vinjavarapu@gmail.com",
  "password": "",
  "returnSecureToken": "true"
})
headers = {
  'Authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjFkMmE2YTZhNDcyYWNhNjNmM2FmNzU2NjIxZjM0Njg2OTI1YjUxYTgiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiUmF2aStWaW5qYXZhcmFwdSIsInBpY3R1cmUiOiJodHRwczovL21lZGlhLnN0YWdpbmcuYXJ0ZW1pcy5pbS91c2Vycy9jZWFiMWRiYS1hZjJmLTQyYjUtYWQ4MC01MzlkMWMxOTE1NDYvcHJvZmlsZS1waG90b3MvY2Y2MTcyY2EtOThhYy00N2NmLTgxODYtNTI0YjI5YTZiNDU4LmpwZWciLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYXJ0ZW1pcy1zdGFnaW5nLTUxNTAyIiwiYXVkIjoiYXJ0ZW1pcy1zdGFnaW5nLTUxNTAyIiwiYXV0aF90aW1lIjoxNjQwOTI5Nzc0LCJ1c2VyX2lkIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsInN1YiI6ImZRelhqSlp0dlJXcW04aWRKQnR3dktHRDgzYzIiLCJpYXQiOjE2NDA5Mjk3NzQsImV4cCI6MTY0MDkzMzM3NCwiZW1haWwiOiJ2aW5qYXZhcmFwdUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMDgwMTg1NTg5ODgyMjIwMjA2MiJdLCJlbWFpbCI6WyJ2aW5qYXZhcmFwdUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.XlNDCkUuRYHWlRK1W1DxR7vUxb17vXA4-2TTLlGqwLP_imWjPINVOlSvtj_nXaDPcZNPH0GH-lrQewSeD34XTnj3L8tlfYKzISb3jRu8bixi_bM6M2AObKG1wLjWq4z0-JoN_u9DXNYlXMoYX9S0p492ttAnTTz2TT6qphNWf63mnd32zL3FkztZo7R5oUbfAvj14Wva6YeQpb51NOUH-oBVRYaEkTBxbiBvqN8xqfehXBIIdqTCf6iiEeLp7CQ1ugT3BBf0FhaVkWTX049vmSmxtJ18m8femFJknekyX-tPBPHBicLB-s5AT5DeJ8UQ-1a6gwViT5XaCxQFgetrSw',
  'Content-Type': 'application/json'
}

def test_LoginWithOutemail():
  response = requests.request("POST", url, headers=headers, data=payload_emptyemail)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 400
  JsonObj = response.json()
  print(JsonObj)
  error_message= JsonObj['error']['message']
  print(error_message)
  assert error_message == "INVALID_EMAIL"

def test_Loginwithoutpassword():
  response = requests.request("POST", url, headers=headers, data=payload_emptypassword)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 400
  JsonObj = response.json()
  print(JsonObj)
  error_message = JsonObj['error']['message']
  print(error_message)
  assert error_message == "MISSING_PASSWORD"





