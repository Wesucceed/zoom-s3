import requests
import os
import json
import time

from base64 import b64encode
from datetime import date
from s3_upload import upload_file_from_stream

from config import config
from dateutil.relativedelta import relativedelta


SERVER_URL = "https://api.zoom.us/v2"
ACCESS_TOKEN_URL = "https://zoom.us/oauth/token"


access_token_auth_val = b64encode(f"{config.client_id}:{config.secret_id}".encode("utf-8"))
access_token_auth_val = f"Basic {access_token_auth_val.decode(encoding='utf-8')}"

ACCESS_HEADER = {
    "Content-Type" : "application/x-www-form-urlencoded",
    "Authorization": access_token_auth_val
}

ACCESS_URL_PARAMETERS = {
    "grant_type" : "account_credentials",
    "account_id" : config.account_id
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


def get_all_recordings(user_email, start_date):
    """
    Gets all recordings from the user account by email
    
    Pre user_email: is a string of the user's email

    Pre start_date: is a list of length 3 representing the start date
                    Date has yy/mm/dd format
    """
    assert isinstance(user_email, str)
    assert isinstance(start_date, list)
    assert len(start_date) == 3
    for _ in start_date:
        assert isinstance(_, int)

    start_date = date(start_date[0], start_date[1], start_date[2])
    
    all_recordings = []
    recording_files_ids = set()
    recordings_url = SERVER_URL + f"/users/{user_email}/recordings"
 
    while start_date < date.today():
       
        end_date = start_date + relativedelta(months=+3)
        rec_auth_val = f"Bearer {get_access_token()}"
        response = requests.get(url = recordings_url, 
                                headers =  {"Authorization" : rec_auth_val},
                                params={
                                    "from" : start_date,
                                    "to" : end_date
                                })
            
        try:
            meetings = response.json().get("meetings", [])
            add_recordings(meetings, recording_files_ids, all_recordings)
        except Exception as e:
            print(e)

        start_date = end_date
      
   
    return all_recordings
        
  

def add_recordings(meetings, recording_files_ids, all_recordings):
     """
     Adds meeting's recordings to all_recordings
     """

     for meeting in meetings:
        folder_name = "kehillah-zoom-to-s3"
        recording_files = meeting.get("recording_files", [])
        for recording_file in recording_files:
            if recording_file.get("id") in recording_files_ids:
                continue
            recording_files_ids.add(recording_file.get("id"))
            download_url = recording_file.get("download_url")
            object_key = f'{meeting.get("topic")}/{meeting.get("start_time")}/{recording_file.get("recording_type")}.{recording_file.get("file_type", "").lower()}'
            all_recordings.append({
                            "download_url" : download_url,
                            "bucket_key" : folder_name,
                            "object_key" : object_key,
                            "meeting_id" : meeting.get("id")
                        })


def write_recording_to_file(data, filename):
    """
    Writes recording data to file

    Pre data: is a list of recording data to be written to file
    
    Pre filename: is a string of the name of the file to be written
    """
    assert isinstance(data, list)
    assert isinstance(filename, str)

    with open(filename, "w") as file:
        json.dump(data, file)
        return True
    

def upload_recording(data):
    """
    Uploads recoding to s3 bucket
    
    Pre data: is the recording data 
    """
    recording_url = f"{data.get('download_url')}?access_key={get_access_token()}"
    bucket_key = data.get("bucket_key")
    object_key = data.get("object_key")
    
    try:
        with requests.get(recording_url, stream = True, allow_redirects = True) as stream:
            
            if stream.status_code != requests.codes.ok:
                print("Not okay", stream.status_code)
                return
            if stream.headers["Content-Type"] == "text/html;charset=utf-8":
                file =  open(f"tmp.html", 'w+')
                print("\n\nCouldn't get the recording.  Check the tmp.html file :(")
                file.write(stream.text)
                file.close()
                return
            
            
            upload_file_from_stream(
                stream = stream.raw,
                bucket_key = bucket_key,
                object_key = object_key,
                content_type = stream.headers["Content-Type"]
            )

    except Exception as e:
        print(
            f"\n\nfailed with error: {e}"
        )
        return 
    return True


def fetch_recordings_and_upload_to_s3():
    """
    Loads recordings from a json file and uploads it to s3

    Calls upload_recording() to upload recordings
    """
    with open(config.file_name, 'r') as file:
        recordings = json.load(file)
        for recording in reversed(recordings):
            
            upload_recording(recording)
            time.sleep(61) 