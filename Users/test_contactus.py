import requests
import json

import Config

url = "https://api.staging.artemis.im/users/contact-us"

users_data = open("users.json","r").read()
headers = {
  'Authorization': Config.token_user,
  'Content-Type': 'application/json'
}

def test_checkstatus():
  response = requests.request("POST", url, headers=headers, data=users_data)
  print(response.status_code)









