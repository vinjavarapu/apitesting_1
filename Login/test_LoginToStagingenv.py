import requests
import json
import Config

Login_data = open("Login_stagenev.json","r").read()
response = requests.request("POST",Config.login_url, headers=Config.headers, data=json.loads(Login_data))
def test_statuccodeofuser():
    response = requests.request("POST", Config.login_url, headers=Config.headers, data=json.loads(Login_data))
    assert response.status_code==200
def test_idTokenexistsin_Responsebody():
    response = requests.request("POST", Config.login_url, headers=Config.headers, data=json.loads(Login_data))
    response_body = response.json()
    assert "idToken" in response_body

def test_emailfieldexists_Responsebody():
    response = requests.request("POST", Config.login_url, headers=Config.headers, data=json.loads(Login_data))
    response_body = response.json()
    assert "email" in response_body
def test_fetchTokenValue():
    response = requests.request("POST", Config.login_url, headers=Config.headers, data=json.loads(Login_data))
    response_body = response.json()
    user_token = response_body['idToken']
    print(user_token)
def test_fetchemailvalueofuser():
    response = requests.request("POST", Config.login_url, headers=Config.headers, data=json.loads(Login_data))
    response_body = response.json()
    user_email = response_body['email']
    print(user_email)
    assert user_email == "vinjavarapu@gmail.com"

def test_displayName():
    response = requests.request("POST", Config.login_url, headers=Config.headers, data=json.loads(Login_data))
    response_body = response.json()
    displayName = response_body['displayName']
    print(displayName)
    assert displayName == "Testing"













