from typing import Optional
from fastapi import FastAPI

# Customize for metavision2
import boto3
import json
from botocore.client import Config

AWS_ACCESS_KEY_ID = 'admin'
AWS_SECRET_ACCESS_KEY = 'lightningdb123'
AWS_BUCKET_PREFIX = ''
ENDPOINT_URL = 'https://minio.k8s.lightningdb:443'

app = FastAPI()


@app.get("/")
def read_root():
    return {"Root": "Data Catalog for Vision Data Lake"}

@app.get("/list/buckets")
def datacatalog_list_existing_buckets():
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, endpoint_url=ENDPOINT_URL, verify=False)
    bucket_list = s3.list_buckets()
    result='['
    for bucket in bucket_list['Buckets']:
        if len(result) > 1:
            result = result + ','
        result = result + ' {' + '"Name":"' +  bucket["Name"] + '"' + '}'
    result = result + ']'
    return json.loads(result)

@app.get("/list/{bucket_name}")
def read_bucket_items(bucket_name: str, q: Optional[str] = None):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, endpoint_url=ENDPOINT_URL, verify=False)
    obj_list = s3.list_objects(Bucket=bucket_name)
    contents_list = obj_list['Contents']
    result='['
    for content in contents_list:
        if len(result) > 1:
            result = result + ','
        content['LastModified'] = content['LastModified'].strftime("%Y-%m-%d %H:%M:%S%z (%Z)")
        result = result + ' ' + json.dumps(content) 
    result = result + ']'
    return json.loads(result)
