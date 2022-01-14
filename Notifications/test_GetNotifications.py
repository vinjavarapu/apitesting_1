import pprint

import requests
import Config
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
  assert titleKey == "notification_member_invited_title"
def test_verifystatusofnotifcation():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print('-----------------------------------------------------------------------------------------')
  status = JsonObj['data'][2]['status']
  assert status == "unviewed"
def test_fetchuuid_notification():
  response = requests.request("GET", url, headers=headers, data=payload)
  JsonObj = response.json()
  print('-----------------------------------------------------------------------------------------')
  uuid = JsonObj['data'][2]['uuid']
  print(uuid)










