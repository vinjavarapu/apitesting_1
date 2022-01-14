import pprint
import requests
import Config
import json
Login_admin = open("Login_admin.json","r").read()
def test_statuscode_valueas200():
    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=json.loads(Login_admin))
    assert response.status_code == 200
def test_idTokenfield_exists():
    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=json.loads(Login_admin))

    response_body = response.json()
    assert "idToken" in response_body
    admin_token = response_body["idToken"]
    print("The token value is",admin_token)

def test_emailvalueofUser():

    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=json.loads(Login_admin))
    response_body = response.json()
    user_email = response_body["email"]
    print(user_email)
    assert user_email == "admin@artemis.im"

def test_displayName_exists():

    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=json.loads(Login_admin))
    response_body = response.json()
    display_name= response_body["displayName"]
    print(display_name)









