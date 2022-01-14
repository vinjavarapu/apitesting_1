################## Admin Config Data####################################

import json


token_admin ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQWRtaW4tc2FuIiwicGljdHVyZSI6Imh0dHBzOi8vZW5jcnlwdGVkLXRibjAuZ3N0YXRpYy5jb20vaW1hZ2VzP3E9dGJuOkFOZDlHY1NLWjFmQzIyNHJWdmtzZzJZZnVWXzBqczZtWnZGenc1dWV6dUFYNGtCUkVXa2lIYzlaIiwicGVybWlzc2lvbnMiOiJlQlVSdEFVRFVhc0FzRXVYcEJLTFVVVVB2WnZhdlh2UHZVckR2UnZPdllxQXVncUJzRHVWckJVWVVCcEVwQ3JBckNLTnVCdkZLSnZjcER2S0tHdkdxRHZXcEF2Q0tEdk10QnZRdVd0Q3NCVVN2SFVadkJ2RHZJcUNLSHZFdWh2U3ZOdkx1ZnZKdlZ2VHREIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL2FydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1ZCI6ImFydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1dGhfdGltZSI6MTY0MjA5NTAwOSwidXNlcl9pZCI6ImxiVGVaNldFMDFSSzN4MkllTVB3cGw2MzJTWTIiLCJzdWIiOiJsYlRlWjZXRTAxUkszeDJJZU1Qd3BsNjMyU1kyIiwiaWF0IjoxNjQyMDk1MDA5LCJleHAiOjE2NDIwOTg2MDksImVtYWlsIjoiYWRtaW5AYXJ0ZW1pcy5pbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBhcnRlbWlzLmltIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.TNmmONsW8PvwDa-IILT9l3KzY6F5AxEH6L-q6pO8b6tOTk900BWS2X4XSV_rGN3oT_S4V8WWvwCLhssyPkvY4DkkhpuCysLXoaeeIV2rRmCVGJbwQqu6tvBGZefNei7ROgumQbJHUA5qpr-wbFqkmoO1yDFJqc0iTKxpjlGEp3HBHb5dyQDywN30lo2duZpolua7sTTFyZbK1XC36H-2uHbF2KxoNlU1ccnXld4mz5sOzjV1QgdXfXJKxxUwGBf8koVMe5jg6UbSKPlsbLXmTKUH8VC1ei2NmWq2YTHQedlMjrg0rkLqNN77KYIapF-uybBH6USs9QrtcpX5Xw9CHw"


admin_headers = {
  'Authorization': token_admin

}

stage_url = "https://api.staging.artemis.im/users/"
payload={}

###############################################################################################################################

############################## Login API to User Data########################################################################

token_user = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVGVzdGluZyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDNGUHU3c1EwQXBUbU9paHBleHIzd2RCMnhOVjMyWHNsYzA1M2hhZz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdWQiOiJhcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdXRoX3RpbWUiOjE2NDIxMzQ3OTksInVzZXJfaWQiOiJmUXpYakpadHZSV3FtOGlkSkJ0d3ZLR0Q4M2MyIiwic3ViIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsImlhdCI6MTY0MjEzNDc5OSwiZXhwIjoxNjQyMTM4Mzk5LCJlbWFpbCI6InZpbmphdmFyYXB1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTEwODAxODU1ODk4ODIyMjAyMDYyIl0sImVtYWlsIjpbInZpbmphdmFyYXB1QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.SrnZZokAzLVVeOhoZSgCGoCNcTHre-XHdnHlTf7zU_34sAznw8sVYCohtpXQnFemTOiwakhPvhU1mn18aY_GZ7U2lUKwj-Ih6_bka3SsBUuLWMIozyLb5suR_kh31U0I1ALRkiSlZlNrqCdu9RbsuOMZMBqs2hA8QkLr_p2cuJa1ZYjyXDgyKXEcN9Fo6c-DO6--x_vLKj2ElIRxwH-pT0tkbZHWLjF9pjvA6oAgVRhEiYgdrDgqCdjvrcQ64qegv5paH6AMCIrAs0U7C4UmoU805OphJlovk1WVyvxxRL3tp3n1S_0ld9YxJLrHr1tmuQNG1GHw2PK524IyTxH5Ig"

login_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBL-odvK_jvqVc5la-PjXVEOc0j25dAfxk"

headers = {
  'Content-Type': 'application/json'
}

#################################################################################################################################

#################### Create Project API #######################################
project_url = "https://api.staging.artemis.im/projects"
payload_projects = json.dumps({
  "title": "V RaviKumar, Relax man"
})

project_headers = {
  'Authorization':  token_user,
  'Content-Type': 'application/json'
}
###########################################################################################################################################

#######################  Retrive All test_Projects ####################################

projects_url = "https://api.staging.artemis.im/projects"

payload_project={}
headers = {
  'Authorization': token_user
}

########################################################################################

####################  Retrieve a Single Project API ################################

retrieveprojectbyid_url = "https://api.staging.artemis.im/projects/339e2755-06ad-4c19-830d-74ccee72b5ef"

singleproject_payload = ""

SingleProject_headers = {
  'Authorization': token_user
}


