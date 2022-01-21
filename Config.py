################## Admin Config Data####################################

import json


token_admin ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwMTU0NmJkMWRhMzA0ZDc2NGNmZWUzYTJhZTVjZDBlNGY2ZjgyN2IiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQWRtaW4tc2FuIiwicGljdHVyZSI6Imh0dHBzOi8vZW5jcnlwdGVkLXRibjAuZ3N0YXRpYy5jb20vaW1hZ2VzP3E9dGJuOkFOZDlHY1NLWjFmQzIyNHJWdmtzZzJZZnVWXzBqczZtWnZGenc1dWV6dUFYNGtCUkVXa2lIYzlaIiwicGVybWlzc2lvbnMiOiJlQlVSdEFVRFVhc0FzRXVYcEJLTFVVVVB2WnZhdlh2UHZVckR2UnZPdllxQXVncUJzRHVWckJVWVVCcEVwQ3JBckNLTnVCdkZLSnZjcER2S0tHdkdxRHZXcEF2Q0tEdk10QnZRdVd0Q3NCVVN2SFVadkJ2RHZJcUNLSHZFdWh2U3ZOdkx1ZnZKdlZ2VHREIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL2FydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1ZCI6ImFydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1dGhfdGltZSI6MTY0Mjc0NzE1MSwidXNlcl9pZCI6ImxiVGVaNldFMDFSSzN4MkllTVB3cGw2MzJTWTIiLCJzdWIiOiJsYlRlWjZXRTAxUkszeDJJZU1Qd3BsNjMyU1kyIiwiaWF0IjoxNjQyNzQ3MTUxLCJleHAiOjE2NDI3NTA3NTEsImVtYWlsIjoiYWRtaW5AYXJ0ZW1pcy5pbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBhcnRlbWlzLmltIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.QEscfmGlNzoZr5xVYMbtOtK1TkuAlKU3e8idQB_359mNgU_WM-GNkYlLWjyuNYxBf0-9uyInxchEuqHl2dS3d5g3EMuPSDsqsYqg8qxL_wqHJvD9ldX0dIDXd6UAiIzRni2VpMiALTiKWwsxYJG5tEqFtHusOK4z3BhlLNUEr5mtMVQOb5krk9jt4mydcUzjlKQ7fnRuwo1_4aqFURG0s_aGhN3LNr4jqyOcTxJ1UW9kZz3cJGfDP5aw4yrhuAM_hR4znpFuHHn_g74NOtLaCRPNPLw4nU184vwbkj81L5zJHgKb5r8EAtxetBAVhZK_unTVBaC5r54hlWv0Rfo5HA"


admin_headers = {
  'Authorization': token_admin

}

stage_url = "https://api.staging.artemis.im/users/"
payload={}

###############################################################################################################################

############################## Login to User Data########################################################################

token_user = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwMTU0NmJkMWRhMzA0ZDc2NGNmZWUzYTJhZTVjZDBlNGY2ZjgyN2IiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiUmF2aSBWaW5qYXZhcmFwdSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDNGUHU3c1EwQXBUbU9paHBleHIzd2RCMnhOVjMyWHNsYzA1M2hhZz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdWQiOiJhcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdXRoX3RpbWUiOjE2NDI3NDcxNDgsInVzZXJfaWQiOiJmUXpYakpadHZSV3FtOGlkSkJ0d3ZLR0Q4M2MyIiwic3ViIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsImlhdCI6MTY0Mjc0NzE0OCwiZXhwIjoxNjQyNzUwNzQ4LCJlbWFpbCI6InZpbmphdmFyYXB1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTEwODAxODU1ODk4ODIyMjAyMDYyIl0sImVtYWlsIjpbInZpbmphdmFyYXB1QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.TuU3BHD54v5_PG8ZDBMZ63liq2xACM88Dnh9DzA86bumyPKzOxjlbwNGDifqKhSKZLqBH9ks7KYQNS4EcvBEYx5PmdcPAtFb2lqf7cckHU_MKFviqSA9Zc7nqlVfPeciPtJPtMi_T68fP9GyId90cwctc6dPMoj_E8sVp9v9uxudLjw0nPed69CCnGUX36-2SBJaMGrWypwqUz89Y8a-xPoQvtqHzepsIOy2IEvV48XX1mChB8WWmbGBMnLNSUsd_IaGqxxrw8p-HHBbYPBXsC41HDB0EawMxBHyPA1g_GrCkeFULJhXbCwloYjJGJlbLNHjmJDvyPsc8uUceb4GiA"

login_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBL-odvK_jvqVc5la-PjXVEOc0j25dAfxk"

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


