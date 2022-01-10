################## Admin Config Data####################################

import json


token_admin ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQWRtaW4tc2FuIiwicGljdHVyZSI6Imh0dHBzOi8vZW5jcnlwdGVkLXRibjAuZ3N0YXRpYy5jb20vaW1hZ2VzP3E9dGJuOkFOZDlHY1NLWjFmQzIyNHJWdmtzZzJZZnVWXzBqczZtWnZGenc1dWV6dUFYNGtCUkVXa2lIYzlaIiwicGVybWlzc2lvbnMiOiJlQlVSdEFVRFVhc0FzRXVYcEJLTFVVVVB2WnZhdlh2UHZVckR2UnZPdllxQXVncUJzRHVWckJVWVVCcEVwQ3JBckNLTnVCdkZLSnZjcER2S0tHdkdxRHZXcEF2Q0tEdk10QnZRdVd0Q3NCVVN2SFVadkJ2RHZJcUNLSHZFdWh2U3ZOdkx1ZnZKdlZ2VHREIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL2FydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1ZCI6ImFydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1dGhfdGltZSI6MTY0MTgzMzI4NiwidXNlcl9pZCI6ImxiVGVaNldFMDFSSzN4MkllTVB3cGw2MzJTWTIiLCJzdWIiOiJsYlRlWjZXRTAxUkszeDJJZU1Qd3BsNjMyU1kyIiwiaWF0IjoxNjQxODMzMjg2LCJleHAiOjE2NDE4MzY4ODYsImVtYWlsIjoiYWRtaW5AYXJ0ZW1pcy5pbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBhcnRlbWlzLmltIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.klisxh6q9okQaALWReY64dJvVvpdSaXVyLb7z3_pP6LGiBK3_iwQynrjl5o9pMrbr77TO-Un4J3U1e0caCNAWizHVEHKdD47uAFsDG4gq-zPG06Tb31UHcmhWrXsSXUX-RFRUPFg7UITTl2eJN_roe3QLdXE1UrU46uWjK3GcH54ooL5PqGF-29KI01MCz19mWqvrEttpSd5Dn0iU1ISDi5aCJGBUdpOvIKaKy4ifoahY5jLe8ottd3hd4OgvRzXIrr3MRARYcK9Vsxydq2DEm_0Y2CyQDfTG5mONJg5TuuUOWKg5FjZEp3uyaH8MZQP8D0-JeK9Rh0v1cmqGHsQQw"


admin_headers = {
  'Authorization': token_admin

}

stage_url = "https://api.staging.artemis.im/users/"
payload={}

###############################################################################################################################

############################## Login to User Data########################################################################

token_user = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVGVzdGluZyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDNGUHU3c1EwQXBUbU9paHBleHIzd2RCMnhOVjMyWHNsYzA1M2hhZz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdWQiOiJhcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdXRoX3RpbWUiOjE2NDE4MzM5NDMsInVzZXJfaWQiOiJmUXpYakpadHZSV3FtOGlkSkJ0d3ZLR0Q4M2MyIiwic3ViIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsImlhdCI6MTY0MTgzMzk0MywiZXhwIjoxNjQxODM3NTQzLCJlbWFpbCI6InZpbmphdmFyYXB1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTEwODAxODU1ODk4ODIyMjAyMDYyIl0sImVtYWlsIjpbInZpbmphdmFyYXB1QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.QBHB6dNi_knN2JnzKUnjyBbdkvRIolwOHpH_8LJwTqA1gZz61VsXiTIq_odoUMdn6vjL6avZUT2DpMUpD4LX9Ch3Zc0Ma9uuegza3EmBPFvefhcRhC9V_JcNlU3KUldlH4wnNjG11RiDUM1suwoNZS3F27S4P3cIRbu1_gbz5xXDVDM47Q3U2Y48vJxuQyVuGi-b9WUVux_uAP-0vSU3nIwou4afm0S3fxMOlvHDeneNWVh6qrj9iLqtytjeRzQa8H6UlUzryfTabWaJHfiMzC5_xgcQ_c6VdvsPtKswy9tn6OqwhQI0Tyy4J3ZKIwoBYL24NJtW4m0vWW2Z1_kp6w"

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


