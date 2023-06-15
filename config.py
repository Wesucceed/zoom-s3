from pydantic import BaseSettings

class Settings(BaseSettings):
    user_email: str
    start_date : str
    end_date : str
    file_name: str
    s3_bucket_access_key: str
    s3_bucket_secret_key: str
    secret_id: str
    client_id: str
    account_id: str
    zoom_webhook_secret_token: str


    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

config = Settings()