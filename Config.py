################## Admin Config Data####################################

import json


token_admin ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQWRtaW4tc2FuIiwicGljdHVyZSI6Imh0dHBzOi8vZW5jcnlwdGVkLXRibjAuZ3N0YXRpYy5jb20vaW1hZ2VzP3E9dGJuOkFOZDlHY1NLWjFmQzIyNHJWdmtzZzJZZnVWXzBqczZtWnZGenc1dWV6dUFYNGtCUkVXa2lIYzlaIiwicGVybWlzc2lvbnMiOiJlQlVSdEFVRFVhc0FzRXVYcEJLTFVVVVB2WnZhdlh2UHZVckR2UnZPdllxQXVncUJzRHVWckJVWVVCcEVwQ3JBckNLTnVCdkZLSnZjcER2S0tHdkdxRHZXcEF2Q0tEdk10QnZRdVd0Q3NCVVN2SFVadkJ2RHZJcUNLSHZFdWh2U3ZOdkx1ZnZKdlZ2VHREIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL2FydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1ZCI6ImFydGVtaXMtc3RhZ2luZy01MTUwMiIsImF1dGhfdGltZSI6MTY0MjE0MzU1NCwidXNlcl9pZCI6ImxiVGVaNldFMDFSSzN4MkllTVB3cGw2MzJTWTIiLCJzdWIiOiJsYlRlWjZXRTAxUkszeDJJZU1Qd3BsNjMyU1kyIiwiaWF0IjoxNjQyMTQzNTU0LCJleHAiOjE2NDIxNDcxNTQsImVtYWlsIjoiYWRtaW5AYXJ0ZW1pcy5pbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBhcnRlbWlzLmltIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.hwfgp17LNisYk_PHynQL1YUFIlrTMUDEDXC_gncdhD2OUFuOHZSadeX0ofEllx706rhKpCDWVY7IZkIlZT1eTr0ppu9ZifmPTUI2W32Zj2yZ5WpQaZpGx2O-9W_OVWo_5DMf22iXvheFYu2b2OPMYjeEvI1FceVzgAYwLN5-aSZTECwO0wtVe491eFDTktIMplzVSz_a6qp7ZLXE1ARm34J3AowNNkMBvKiGvgWv4dCSdqDmQwruMpysBIzJeBVXoH3fad-Qyo_uTy602V-eG54qcJCaXuYoMKON4kGXEoCaAMxDV3GZxs03Ym4lZNdJNLf_qOyCrMslSDieiIkItw"


admin_headers = {
  'Authorization': token_admin

}

stage_url = "https://api.staging.artemis.im/users/"
payload={}

###############################################################################################################################

############################## Login to User Data########################################################################

token_user = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjM1MDZmMzc1MjI0N2ZjZjk0Y2JlNWQyZDZiNTlmYThhMmJhYjFlYzIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiam9zZWVlZWVlIFJpemFsIDIiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2gzRlB1N3NRMEFwVG1PaWhwZXhyM3dkQjJ4TlYzMlhzbGMwNTNoYWc9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYXJ0ZW1pcy1zdGFnaW5nLTUxNTAyIiwiYXVkIjoiYXJ0ZW1pcy1zdGFnaW5nLTUxNTAyIiwiYXV0aF90aW1lIjoxNjQyMTY2MTg2LCJ1c2VyX2lkIjoiZlF6WGpKWnR2UldxbThpZEpCdHd2S0dEODNjMiIsInN1YiI6ImZRelhqSlp0dlJXcW04aWRKQnR3dktHRDgzYzIiLCJpYXQiOjE2NDIxNjYxODYsImV4cCI6MTY0MjE2OTc4NiwiZW1haWwiOiJ2aW5qYXZhcmFwdUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMDgwMTg1NTg5ODgyMjIwMjA2MiJdLCJlbWFpbCI6WyJ2aW5qYXZhcmFwdUBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.HQgmRUY9VSHBwKG_Wpt9RmPKbF5ZKrHqoGOHau4FMjxBUnsKfjrb2_yRoVQ8yEBxqznj4lcmj4ABCIAoIHZg2D-OKZVqJ4N3Zy5DUdlRBHs600eRPhtejljPjjCYRrm35a2Wz3y2zcy0bRgpOhFDAdJ2a5DmdhzMWM5T9jA0FCTQq9Jgaa_w3gAmAaq78OVu7V_aMzT7qcOBX0tCNJhCCNseRyDlifSpkt1zt3-VoqLAQwUeZpHPcYTFDwswaPlbslryNuVVTOcA5Tr9DlBELeTa__5enylcQFj2OqRP1WJMRNQdIZ8Pk1cdUqQoUtJG13aDokeAOD_dPNaG3MR0ig"

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


