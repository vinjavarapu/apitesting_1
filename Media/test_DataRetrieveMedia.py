import pprint
from apitesting_1 import Config
import requests

url = "https://media.staging.artemis.im/banners/projects/c074009e-6a12-46b1-a4db-8136c8659c5c.jpg?Expires=1642236272&Key-Pair-Id=APKAIKTLL764YZKS2MRQ&Signature=VOgA0Clfc-Vt6uAYQlkMFMzVWjRfkajv-cMx-xqxwiVFXkJ~YbzrocD65pZPX5WGIfL1T6GkDVoEmBCqbY~Pzs0XX94QQ0v76Q~RdTXKQJ5nshPxEZV5CHYbOZks3ly6jMeKbbzfWToNSs-qTzjSu~igUj6PTTXLRrcVsoI8XL1kAAsSBNW~89H8fW6v7Qx-MYHbBJLydmFPkK9urWEuOzo6gTelWY-PSRJORRPeoFgjmMVMpx597bfm5qgBlA0-xIYYQmtXeG7Eii9tArqIJGJiLmZMAGFingIrUmqy-euqJteI-3ZpxAn2lw-qRYRB~iZ5RAOQZ6tzyi6GPQMOzw__"

payload={}
headers = {}

def test_statuscheckcode():
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    assert response.status_code == 200, "Invalid firebase login"
def test_retrievebody():
    response = requests.request("GET", url, headers=headers, data=payload)
    JsonObj = response.content






