from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Customize for metavision2
import boto3
import json
from botocore.client import Config

AWS_ACCESS_KEY_ID = 'admin'
AWS_SECRET_ACCESS_KEY = 'lightningdb123'
AWS_BUCKET_NAME = 'ai-hub'
AWS_BUCKET_PREFIX = ''
ENDPOINT_URL = 'https://minio.k8s.lightningdb:443'

def datacatalog_list(request):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, endpoint_url=ENDPOINT_URL, verify=False)
    obj_list = s3.list_objects(Bucket=AWS_BUCKET_NAME)
    contents_list = obj_list['Contents']
    result='['
    for content in contents_list:
        if len(result) > 1:
            result = result + ','
        content['LastModified'] = content['LastModified'].strftime("%Y-%m-%d %H:%M:%S%z (%Z)")
        result = result + ' ' + json.dumps(content) 
    result = result + ']'
    return HttpResponse(result)
