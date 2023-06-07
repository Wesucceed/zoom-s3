import requests
import json
import boto3
import os
import base64

# https://zoom.us/oauth/authorize?response_type=code&client_id=X_U_1WfcTLST6tEiVs3Pkw&redirect_uri=http://localhost:3000/redirect
SERVER_URL = "https://api.zoom.us/v2"
LIST_OF_RECORDINGS_URL = "/users/{userId}/recordings"


AUTH_URL = "https://zoom.us/oauth/authorize"
auth_query_parameters = {
    "response_type" : "code",
    "redirect_uri" : "http://localhost:3000/redirect",
    "client_id" : "X_U_1WfcTLST6tEiVs3Pkw"
}

ACCESS_TOKEN_URL = "https://zoom.us/oauth/token"

CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")

authorization_header_value = base64.b64encode(f"{CLIENT_ID}:{SECRET_ID}".encode()).decode()

ACCESS_HEADER = {
    "Host" : "zoom.us",
    "Authorization": f"Basic {authorization_header_value}",
    "Content-Type": "application/x-www-form-urlencoded"
}


def get_all_recordings(userId):
    """
    Gets all recordings from the user account
    
    Parameter userId: is an integer representing the user id
    """
    userId = ''
    recordings_url = 'https://api.zoom.us/v2/users/' + userId + '/recordings'
    response = requests.get(recordings_url)

    # Using the meetings property, we access the value which returns a list of recordings
    recording_info = response.json()['meetings'] 
    return recording_info


def get_auth_code():
    """
    Returns the authorization code of the user
    """
    login_url = requests.get(url = AUTH_URL, params = auth_query_parameters)
    print(login_url.url)

ACCESS_URL_PARAMETERS = {
    "code" : get_auth_code(),
    "grant_type" : "- authorization_code",
    "redirect_uri" : "http://localhost:3000/redirect"
}


def get_access_token():
    """
    Returns the access token of the user
    """
    access_token_response = requests.post(ACCESS_TOKEN_URL, params=ACCESS_URL_PARAMETERS, headers=ACCESS_HEADER)

    if access_token_response.status_code == 200:
        access_token = access_token_response.json()["access_token"]
        print(f"Access Token: {access_token}")
    else:
        print(access_token_response.url)
        print("Failed to obtain access token.")


# return links to videos
all_recordings = ["all recordings available"]
def login(login_url, email, password):
    """
    Signs in to user account
    """
    payload = {
        "email" : email,
        "password" : password
    }
    code = requests.request(method="post", url = login_url, json=login_url)
    print(code.url)

get_access_token()
# get_auth_code()


    

access_key = ''
secret_key = ''
bucket = ''

# Creating the s3 client
s3_client = boto3.client('s3', aws_access_key=access_key, aws_secret_access_key=secret_key)


for recording in all_recordings:
    # Using the put_object method 
    s3_client.put_object(Body=..., Bucket=bucket, Key='')
    print("Recording has been successfully uploaded to s3")





