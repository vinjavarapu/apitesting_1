import pprint
import requests
from apitesting_1 import Config
import json

def test_statuscodeof_requestis200():
    response = requests.request("POST", Config.project_url, headers=Config.project_headers,
                                data=Config.payload_projects)
    assert response.status_code == 201

def test_verifyProjectStatus():
    response = requests.request("POST", Config.project_url, headers=Config.project_headers,
                                data=Config.payload_projects)
    response_body = response.json()
    project_status = response_body["data"]["status"]
    assert project_status == "draft"

def test_VerifyProjectTitle():

    response = requests.request("POST", Config.project_url, headers=Config.project_headers,
                                data=Config.payload_projects)
    response_body = response.json()
    project_title = response_body["data"]["title"]
    print(project_title)
    assert project_title == "V RaviKumar, Relax man"

def test_VerifyProject_OwnerName():

    response = requests.request("POST", Config.project_url, headers=Config.project_headers,
                                data=Config.payload_projects)
    response_body = response.json()
    project_owner = response_body["data"]["owner"]["displayName"]
    print(project_owner)
    #assert project_owner == "ManiR"

def test_projectUUIDValue_is():
    response = requests.request("POST", Config.project_url, headers=Config.project_headers,
                                data=Config.payload_projects)
    response_body = response.json()
    project_uuid = response_body['data']['uuid']
    print(project_uuid)

def test_Project_AccessPolicy():
    response = requests.request("POST", Config.project_url, headers=Config.project_headers,
                                data=Config.payload_projects)
    response_body = response.json()
    project_acesspolicy = response_body['data']['accessPolicy']
    print(project_acesspolicy)











