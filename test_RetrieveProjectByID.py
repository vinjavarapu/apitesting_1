import requests
import Config


def test_retrieveproject_byID_statusCode():
    response = requests.request("GET", Config.retrieveprojectbyid_url, headers=Config.SingleProject_headers,
                                data=Config.singleproject_payload)
    assert response.status_code == 200


def test_checkContentType():
    response = requests.request("GET", Config.retrieveprojectbyid_url, headers=Config.SingleProject_headers,
                                data=Config.singleproject_payload)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


### Check the Name field exists #########################################

def test_displayNameField_exists():
    response = requests.request("GET", Config.retrieveprojectbyid_url, headers=Config.SingleProject_headers,
                                data=Config.singleproject_payload)
    response_body = response.json()
    assert "displayName" in response_body["data"]["owner"]
    assert response_body["data"]["owner"]["displayName"] == "ManiR"


def test_titleof_project():
    response = requests.request("GET", Config.retrieveprojectbyid_url, headers=Config.SingleProject_headers,
                                data=Config.singleproject_payload)
    response_body = response.json()
    assert response_body["data"]["title"] == "V RaviKumar, Relax man"

def test_status_of_project():

    response = requests.request("GET", Config.retrieveprojectbyid_url, headers=Config.SingleProject_headers,
                                data=Config.singleproject_payload)
    response_body = response.json()
    project_status = response_body["data"]["status"]
    print('The project status is', project_status)
    assert project_status == "draft"



