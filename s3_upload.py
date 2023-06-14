import boto3
import os
from dotenv import load_dotenv
load_dotenv()



ACCESS_KEY = os.environ.get('S3_BUCKET_ACCESS_KEY')
SECRET_KEY = os.environ.get('S3_BUCKET_SECRET_KEY')


def get_s3_client():

    return boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )


def upload_file_from_stream(
  stream,
  bucket_key:str,
  object_key: str,
  content_type: str
) -> None:
    s3_client = get_s3_client()

    print(bucket_key, content_type)
    
    s3_client.upload_fileobj(
    stream,
    bucket_key,
    object_key,
    ExtraArgs={"ContentType": content_type}
  )
    print("In progress...")
    return True
