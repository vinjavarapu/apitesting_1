import requests
import Config
import json

url = "https://api.staging.artemis.im/notifications?app=organizer"

payload={}
headers = {
  'Authorization': Config.token_user
}

def test_statuscodecheck():
    response = requests.request("GET", url, headers=headers, data=payload)
    statuscode = response.status_code
    assert statuscode == 200
def test_verifyapp():
    response = requests.request("GET", url, headers=headers, data=payload)
    Jsonobj = response.json()
    app = Jsonobj['data'][0]['app']
    print('The app type is ' , app)
    assert app == "organizer"
def test_testtitleofnotification():
    response = requests.request("GET", url, headers=headers, data=payload)
    Jsonobj = response.json()
    title = Jsonobj['data'][0]['data']['title']
    print('The title of notification  is ', ""  + str(title))





