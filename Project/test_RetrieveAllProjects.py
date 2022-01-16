import pprint

import requests
from apitesting_1 import Config


def test_statuscodeis_200():
    response = requests.request("GET", Config.project_url, headers=Config.project_headers, data=Config.payload_projects)
    assert response.status_code == 200

def test_responsebdyContents():
    response = requests.request("GET", Config.project_url, headers=Config.project_headers, data=Config.payload_projects)

    response_body = response.json()
    print(response_body)

def test_datafieldexistsinResponsebody():
    response = requests.request("GET", Config.project_url, headers=Config.project_headers, data=Config.payload_projects)

    response_body = response.json()
    assert "data" in response_body

def test_displayName_firestrecord():

    response = requests.request("GET", Config.project_url, headers=Config.project_headers, data=Config.payload_projects)
    response_body = response.json()
    displayName = response_body['data'][0]['owner']['displayName']
    assert displayName == "GARIMA"








