import pprint
import requests
import Config
import json
response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=Config.admin_payload)
JsonObj = response.json()
pprint.pprint(JsonObj)
token_admin = JsonObj['idToken']
print(token_admin)
configfile = open("Config1.txt","a")
configfile.write("admin_token" + "= "+ str(token_admin))
def test_statuscode_valueas200():
    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=Config.admin_payload)
    assert response.status_code == 200
def test_idTokenfield_exists():
    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=Config.admin_payload)

    response_body = response.json()
    assert "idToken" in response_body
    admin_token = response_body["idToken"]
    print("The token value is",admin_token)

def test_emailvalueofUser():

    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=Config.admin_payload)
    response_body = response.json()
    user_email = response_body["email"]
    print(user_email)
    assert user_email == "admin@artemis.im"

def test_displayName_exists():

    response = requests.request("POST", Config.login_url, headers=Config.admin_headers, data=Config.admin_payload)
    response_body = response.json()
    display_name= response_body["displayName"]
    print(display_name)









