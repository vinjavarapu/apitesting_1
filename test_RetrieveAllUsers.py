import pprint
import Config
import requests
response = requests.request("GET", Config.stage_url, headers=Config.admin_headers, data=Config.payload)
JsonObj = response.json()
pprint.pprint(JsonObj)
FirstRecord = JsonObj['data'][0]
print("######################## First record Data ###############################")
pprint.pprint(FirstRecord)




