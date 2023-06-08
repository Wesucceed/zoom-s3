import requests
import os
from base64 import b64encode

from dotenv import load_dotenv
load_dotenv()

SERVER_URL = "https://api.zoom.us/v2"

ACCESS_TOKEN_URL = "https://zoom.us/oauth/token"


CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET_ID = os.environ.get("SECRET_ID")

auth_value = b64encode(f"{CLIENT_ID}:{SECRET_ID}".encode("utf-8"))
auth_value = auth_value.decode(encoding="utf-8")

ACCESS_HEADER = {
    "Content-Type" : "application/x-www-form-urlencoded",
    "Authorization": f"Basic {auth_value}"
}

ACCESS_URL_PARAMETERS = {
    "grant_type" : "account_credentials",
    "account_id" : os.environ.get("ACCOUNT_ID")
}


def get_access_token():
    """
    Returns the access token of the user
    """
    access_token_response = requests.post(ACCESS_TOKEN_URL, 
                                          data = ACCESS_URL_PARAMETERS, 
                                          headers = ACCESS_HEADER)

    if access_token_response.status_code == 200:
        access_token = access_token_response.json()["access_token"]
        return access_token
    
    print("Failed to obtain access token.")


def get_all_recordings(userId):
    """
    Gets all recordings from the user account
    
    Parameter userId: is an integer representing the user id
    """
    recordings_url = SERVER_URL + f"/users/{userId}/recordings"
    response = requests.get(recordings_url)
    if response.status_code == 200:
        return response.json()['meetings'] 
    else:
        print("Failed to get recordings")

