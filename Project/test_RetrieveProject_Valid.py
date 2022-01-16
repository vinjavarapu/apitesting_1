import pprint
import requests
from apitesting_1 import Config
response = requests.request("GET", Config.retrieveprojectbyid_url, headers=Config.SingleProject_headers, data=Config.singleproject_payload)
JsonObj = response.json()
pprint.pprint(JsonObj)