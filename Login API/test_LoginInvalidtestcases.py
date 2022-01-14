import requests
import json
import Config



url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBL-odvK_jvqVc5la-PjXVEOc0j25dAfxk"

Login_InvalidData = open("InvalidLoginData.json","r").read()
Login_InvalidData1 = open("InvalidLoginData1.json","r").read()

headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

def test_LoginWithOutemail():
  response = requests.request("POST", url, headers=headers, data=Login_InvalidData)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 400
  JsonObj = response.json()
  print(JsonObj)
  error_message= JsonObj['error']['message']
  print(error_message)
  assert error_message == "INVALID_EMAIL"

def test_Loginwithoutpassword():
  response = requests.request("POST", url, headers=headers, data=Login_InvalidData1)
  statuscode = response.status_code
  print(statuscode)
  assert statuscode == 400
  JsonObj = response.json()
  print(JsonObj)
  error_message = JsonObj['error']['message']
  print(error_message)
  assert error_message == "MISSING_PASSWORD"





