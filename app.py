import requests
import json
import boto3

# https://zoom.us/oauth/authorize?response_type=code&client_id=X_U_1WfcTLST6tEiVs3Pkw&redirect_uri=http://localhost:3000/redirect
SERVER_URL = "https://api.zoom.us/v2"
LIST_OF_RECORDINGS_URL = "/users/{userId}/recordings"


AUTH_URL = "https://zoom.us/oauth/authorize"
auth_query_parameters = {
    "response_type" : "code",
    "redirect_uri" : "http://localhost:3000/redirect",
    "client_id" : "X_U_1WfcTLST6tEiVs3Pkw"
}


# ACCESS_TOKEN_URL = "https://zoom.us/oauth/token"
# access_url = {
#     "code":,
#     "grant_type" : "- authorization_code",
#     "redirect_uri" : "http://localhost:3000/redirect"
# }

# access_header = {
#     "Authorization" : " Q2xpZW50X0lEOkNsaWVudF9TZWNyZXQ=.",
#     "Content-Type" : "application/x-www-form-urlencoded"
# }

def get_all_recordings(userId):
    """
    Gets all recordings from the user account
    
    Parameter userId: is an integer representing the user id
    """


def get_auth_code():
    """
    Returns the authorization code of the user
    """
    login_url = requests.request(method = "get", url = AUTH_URL, params = auth_query_parameters)
    print(login_url.url)
    # login(login_url, "mensahjephthah159@gmail.com", "jephmens041")


def get_access_token():
    """
    Returns the access token of the user
    """

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


get_auth_code()


    

all_recordings = "all recordings available"

# Creating the s3 client
s3_client = boto3.client('s3')


bucket = ''


for recording in all_recordings:
    # Using the put_object method 
    s3_client.put_object(Body=..., Bucket=bucket, Key='')
