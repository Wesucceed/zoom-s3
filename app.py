import requests
import boto3


SERVER_URL = "https://api.zoom.us/v2"
LIST_OF_RECORDINGS_URL = "/users/{userId}/recordings"


AUTH_URL = "https://zoom.us/oauth/authorize"
auth_parameters = {
    "response_type" :,
    "redirect_uri" :,
    "client_id" : 
}
auth_header = {
    "Authorization",
    "Content-Type"
}


ACCESS_TOKEN_URL = "https://zoom.us/oauth/token"
access_url = {
    "code":,
    "grant_type"
}

def get_all_recordings(userId):
    """
    Gets all recordings from the user account
    
    Parameter userId: is an integer representing the user id
    """


def get_auth_code():
    """
    Returns the authorization code of the user
    """

def get_access_token():
    """
    Returns the access token of the user
    """


all_recordings = "all recordings available"

# Creating the s3 client
s3_client = boto3.client('s3')


bucket = ''


for recording in all_recordings:
    # Using the put_object method 
    s3_client.put_object(Body=..., Bucket=bucket, Key='')