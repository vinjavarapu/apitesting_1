import requests

from apitesting_1 import Config

url = "https://api.staging.artemis.im/users/_me"

payload = "{\n    \"subscriptionTier\":\"enterprise\",\n    \"subscriptionExpiry\": \"2021-03-26T00:00:00.000+08:00\"\n}"
headers = {
  'authority': 'api.dev.artemis.im',
  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
  'accept': 'application/json, text/plain, */*',
  'authorization': Config.token_user,
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
  'content-type': 'application/json;charset=UTF-8',
  'origin': 'https://admin.dev.artemis.im',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://admin.dev.artemis.im/',
  'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,fil;q=0.6,id;q=0.5'
}

def test_statuccheckcode():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  print(response.status_code)
  assert response.status_code == 200
def test_fetchresponsebody():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  print(JsonObj)
def test_NumberofProjectsCreated():
  response = requests.request("PATCH", url, headers=headers, data=payload)
  JsonObj = response.json()
  projectsCreated = JsonObj['result']['projectsCreated']
  print("Total number of projects created", projectsCreated)





