"""
Stream zoom recordings to an S3 bucket
"""
import zoom
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    user_email = os.environ.get("USER_EMAIL")
    start_date = os.environ.get("START_DATE").split("-")
    start_date = [int(start_date[0]), int(start_date[1]), int(start_date[2])]

 
    res = zoom.get_all_recordings(user_email, start_date)
    zoom.write_recording_to_file(res,
                            os.environ.get("FILENAME"))
    zoom.fetch_recordings_and_upload_to_s3()
    print("SCRIPT EXECUTED SUCCESSFULY: Upload complete!")


