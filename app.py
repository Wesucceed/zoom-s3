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
    login_url = requests.request(method = "get", url = AUTH_URL, params = auth_query_parameters)
    print(login_url.url)
    # login(login_url, "mensahjephthah159@gmail.com", "jephmens041")


def get_access_token():
    """
    Returns the access token of the user
    """

<<<<<<< HEAD
# return links to videos
all_recordings = ["all recordings available"]
=======
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


    
>>>>>>> e29ad44806b7972ed7e6cee7f2d68a0d58eb501b

access_key = ''
secret_key = ''
bucket = ''

# Creating the s3 client
s3_client = boto3.client('s3', aws_access_key=access_key, aws_secret_access_key=secret_key)


for recording in all_recordings:
    # Using the put_object method 
    s3_client.put_object(Body=..., Bucket=bucket, Key='')
<<<<<<< HEAD
    print("Recording has been successfully uploaded to s3")
=======
>>>>>>> e29ad44806b7972ed7e6cee7f2d68a0d58eb501b
