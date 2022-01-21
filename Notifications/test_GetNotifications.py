import pprint

import requests
from apitesting_1 import Config
import json

url = "https://api.staging.artemis.im/notifications"

payload={}
headers = {
  'Authorization': Config.token_user
}

def test_statuscheckcode():
  response = requests.request("GET", url, headers=headers, data=payload)
  statuscode = response.status_code
  assert statuscode == 200
def test_fetchresponsebody():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  pprint.pprint(JsonObj)
  print('-----------------------------------------------------------------------------------------')
  print(JsonObj['data'][2]['data']['body'])
def test_fetchtitleKey():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print('-----------------------------------------------------------------------------------------')
  titleKey = JsonObj['data'][2]['data']['titleKey']
  assert titleKey == "notification_new_member_invite_title"
def test_verifystatusofnotifcation():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print('-----------------------------------------------------------------------------------------')
  status = JsonObj['data'][2]['status']
  assert status == "viewed"
def test_fetchuuid_notification():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print('-----------------------------------------------------------------------------------------')
  uuid = JsonObj['data'][2]['uuid']
  print(uuid)










