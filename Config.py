################## Admin Config Data####################################

import json


token_admin ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQWRtaW4tc2FuIiwicGljdHVyZSI6Imh0dHBzOi8vZW5jcnlwdGVkLXRibjAuZ3N0YXRpYy5jb20vaW1hZ2VzP3E9dGJuOkFOZDlHY1NLWjFmQzIyNHJWdmtzZzJZZnVWXzBqczZtWnZGenc1dWV6dUFYNGtCUkVXa2lIYzlaIiwicGVybWlzc2lvbnMiOiJlQlVSdEFVRFVhc0FzRXVYcEJLTFVVVVB2WnZhdlh2UHZVckR2UnZPdllxQXVncUJzRHVWckJVWVVCcEVwQ3JBckNLTnVCdkZLSnZjcER2S0tHdkdxRHZXcEF2Q0tEdk10QnZRdVd0Q3NCVVN2SFVadkJ2RHZJcUNLSHZFdWh2U3ZOdkx1ZnZKdlZ2VHREIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL2FydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1ZCI6ImFydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1dGhfdGltZSI6MTY0MTYyMjkwOSwidXNlcl9pZCI6ImxiVGVaNldFMDFSSzN4MkllTVB3cGw2MzJTWTIiLCJzdWIiOiJsYlRlWjZXRTAxUkszeDJJZU1Qd3BsNjMyU1kyIiwiaWF0IjoxNjQxNjIyOTA5LCJleHAiOjE2NDE2MjY1MDksImVtYWlsIjoiYWRtaW5AYXJ0ZW1pcy5pbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBhcnRlbWlzLmltIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.gHjgbVGj7xOgWEuhPaQOH-krIUL0ROXlfmIa1EDNav_0qsOKkwZI1kJAMGag2vIMLteqv15PiB4rqoq4QAwWr2lPTopX0B3L4TejzWoyy-XC-ms3vfat001Chl2rV44wP7w1RT9NqN5AnFxzwOf37TD6OjDJMMEH2HjE5FV0u8-mWpzijkAz9zLr2zE9dvlEqB9lMdSrUm8R7095W_Vn3n6PDYDnsFJmENUhw4ilJARX3mvaENfvEygIZzuiNqmKte2PCmcmzHbE25Eu4r1jwhb7LpDIHnojN700yOSFS2uc4jPtrTx76K9eTg4zKEjxavvHZROTrM3H88587zDwNg"


admin_headers = {
  'Authorization': token_admin}
admin_payload = json.dumps({
  "email": "admin@artemis.im",
  "password": "4dminP@ssw0rd",
  "returnSecureToken": "true"
})
stage_url = "https://api.staging.artemis.im/users/"
payload={}

###############################################################################################################################

############################## Login to User Data########################################################################

token_user = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVGVzdGluZyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDNGUHU3c1EwQXBUbU9paHBleHIzd2RCMnhOVjMyWHNsYzA1M2hhZz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdWQiOiJhcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdXRoX3RpbWUiOjE2NDE2MjI4NDMsInVzZXJfaWQiOiJmUXpYakpadHZSV3FtOGlkSkJ0d3ZLR0Q4M2MyIiwic3ViIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsImlhdCI6MTY0MTYyMjg0MywiZXhwIjoxNjQxNjI2NDQzLCJlbWFpbCI6InZpbmphdmFyYXB1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTEwODAxODU1ODk4ODIyMjAyMDYyIl0sImVtYWlsIjpbInZpbmphdmFyYXB1QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.YMdWq9iL3_7r1IXqcwm5lBKpKIxcbROL7M-3LHqLoHsfDerVqNBDB8OqAAVmapuDV5PgfgquJiqWVkoyDK-jHKFYAERLHDLsuy6YfF2aZPO0k14eeh-gzo5IztY_LhkZYvDUnxNKth2mDVCc9upW_nP1Mo32n43rBMphlOWQJj2dhEjKfnCrvejG7bRwRhrvJrgQqJe6O4Gcu6q1o8NldY2AeoCzDrlj9jlnQd-qw84TaRTac_En_UXBFj04jDVriksl6_dJlBOSySkqFue3ZIEzYFuOCjsLVofVScWwUWioWGg3SSCLocJdap3fFWPS5OQGAUI8hFv4ACGvK1SQiQ"

login_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBL-odvK_jvqVc5la-PjXVEOc0j25dAfxk"
login_payload = json.dumps({
  "email": "vinjavarapu@gmail.com",
  "password": "Ravi@123",
  "returnSecureToken": "true"
})
headers = {
  'Content-Type': 'application/json'
}

#################################################################################################################################

#################### Create Project #######################################
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

####################  Retrieve a Single Project ################################

retrieveprojectbyid_url = "https://api.staging.artemis.im/projects/339e2755-06ad-4c19-830d-74ccee72b5ef"

singleproject_payload = ""

SingleProject_headers = {
  'Authorization': token_user
}


