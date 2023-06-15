import os
import boto3  
from config import config
# from dotenv import load_dotenv
# load_dotenv()


def get_s3_client():

    return boto3.client(
        's3',
        aws_access_key_id=config.s3_bucket_access_key,
        aws_secret_access_key=config.s3_bucket_secret_key
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
