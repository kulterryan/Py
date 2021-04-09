import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
SENCE_PATH = os.getenv('SENCE_PATH')

print(str(STORAGE_BUCKET_NAME))
print(str(SENCE_PATH))
