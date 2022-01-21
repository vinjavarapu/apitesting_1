################## Admin Config Data####################################

import json
import requests


token_admin ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwMTU0NmJkMWRhMzA0ZDc2NGNmZWUzYTJhZTVjZDBlNGY2ZjgyN2IiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQWRtaW4tc2FuIiwicGljdHVyZSI6Imh0dHBzOi8vZW5jcnlwdGVkLXRibjAuZ3N0YXRpYy5jb20vaW1hZ2VzP3E9dGJuOkFOZDlHY1NLWjFmQzIyNHJWdmtzZzJZZnVWXzBqczZtWnZGenc1dWV6dUFYNGtCUkVXa2lIYzlaIiwicGVybWlzc2lvbnMiOiJlQlVSdEFVRFVhc0FzRXVYcEJLTFVVVVB2WnZhdlh2UHZVckR2UnZPdllxQXVncUJzRHVWckJVWVVCcEVwQ3JBckNLTnVCdkZLSnZjcER2S0tHdkdxRHZXcEF2Q0tEdk10QnZRdVd0Q3NCVVN2SFVadkJ2RHZJcUNLSHZFdWh2U3ZOdkx1ZnZKdlZ2VHREIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL2FydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1ZCI6ImFydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1dGhfdGltZSI6MTY0MjI0ODc1OSwidXNlcl9pZCI6ImxiVGVaNldFMDFSSzN4MkllTVB3cGw2MzJTWTIiLCJzdWIiOiJsYlRlWjZXRTAxUkszeDJJZU1Qd3BsNjMyU1kyIiwiaWF0IjoxNjQyMjQ4NzU5LCJleHAiOjE2NDIyNTIzNTksImVtYWlsIjoiYWRtaW5AYXJ0ZW1pcy5pbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBhcnRlbWlzLmltIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.fzFh4UUJ3UzYxK8F4bu0b7iucu4ZGksS1MTw19c7Xm3t6mimGmg0F8GXJkrs6UR-qFI9y_7IVke8GDY2GRNj0e_NjKr-28eE2z6_R1acirUOVF0eOF4QexKfaLUcXH4E_lq2xdeLK6ea6XdI-i1MBXbXrLe5SDrcWk7XpCya8R8xLMRSrdcMtJYNV_12SHSfD9xKpOxPRhdarfbAQ7Yr1kfZVLpIa73kOarMgDlgg84QwG_SxX6BvDXkvIHmYXuml2yQhfvjHdJ3hRfWTeWzKhLROmVHJ2x6Hot5UboMOqi-_JhwvBXCUCCbtTwU-PizO85_txz6BfeHnAnjePiqYA"

token_user = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwMTU0NmJkMWRhMzA0ZDc2NGNmZWUzYTJhZTVjZDBlNGY2ZjgyN2IiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiUmF2aSBWaW5qYXZhcmFwdSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDNGUHU3c1EwQXBUbU9paHBleHIzd2RCMnhOVjMyWHNsYzA1M2hhZz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdWQiOiJhcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdXRoX3RpbWUiOjE2NDI3NDY4ODMsInVzZXJfaWQiOiJmUXpYakpadHZSV3FtOGlkSkJ0d3ZLR0Q4M2MyIiwic3ViIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsImlhdCI6MTY0Mjc0Njg4MywiZXhwIjoxNjQyNzUwNDgzLCJlbWFpbCI6InZpbmphdmFyYXB1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTEwODAxODU1ODk4ODIyMjAyMDYyIl0sImVtYWlsIjpbInZpbmphdmFyYXB1QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.EDgOQ5BTK22mXokqye-MUcI9uYbFAgNChOZPKliSG72mX1apDkokOQTDIXAUKXNevTTvXAlEp7f-PYuFJ4KDALRogaU7KoDvwH6ij0JeFgQpHwEFcovYif5YCgxIABEH153HQ3B2muBw3jxTn6Uh5rs09vzpLVVbKgSJOaKM-OeHzn6UCtAnGJafOI06A3nLjMIpG0lOzlfH8AWw6cdmQRVSsDbksdWQac6F2_YY2QzNytIKChtQQ13OsnQsXkCVlcrWGSQ9K7OllRQj0NEM1bdxo8ydNP7uG57yNEUnHc9MQIkP-bcUfWblRCQlhW6Is3rN-o4bLKY3HOt1kmxt8w"
admin_headers = {
  'Authorization': token_admin

}

stage_url = "https://api.staging.artemis.im/users/"
payload={}

###############################################################################################################################

############################## Login to User Data########################################################################oken_user = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjQwMTU0NmJkMWRhMzA0ZDc2NGNmZWUzYTJhZTVjZDBlNGY2ZjgyN2IiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiUmF2aSBWaW5qYXZhcmFwdSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDNGUHU3c1EwQXBUbU9paHBleHIzd2RCMnhOVjMyWHNsYzA1M2hhZz1zOTYtYyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdWQiOiJhcnRlbWlzLXN0YWdpbmctNTE1MDIiLCJhdXRoX3RpbWUiOjE2NDIyNDcxNDIsInVzZXJfaWQiOiJmUXpYakpadHZSV3FtOGlkSkJ0d3ZLR0Q4M2MyIiwic3ViIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsImlhdCI6MTY0MjI0NzE0MiwiZXhwIjoxNjQyMjUwNzQyLCJlbWFpbCI6InZpbmphdmFyYXB1QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTEwODAxODU1ODk4ODIyMjAyMDYyIl0sImVtYWlsIjpbInZpbmphdmFyYXB1QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.zCEG8hjsu4uasdPDccAGHGP36jRf0Itq8ns34Rtg-roGH8Xr66Cqp0NAvHJ_lwu2cjUNillwJOGaOsYznyhno0RrTqnoJK2j_rpSrvSNqy0ScgbCXgqaOmicnOLepok73lwChtakCm07-GcIJPwbSVp3hwshKZbBqsCaoJrree5wN7cair6QwxBe3la2kVkuMA-K_C29CAexfnZM2su2zTu3zQHbYqKuwpZzvRGQpHemSHrBRUsNyVPcn_4PXQ7fobj5slL0FR_80XpHdxI-1g9zKxW4_ch49EvdPTHqleFZqlfVWttLnCSB69l-3GosQXASW8Hx9pJOjaOfOrTcCA"

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


