from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Customize for metavision2
import boto3
import json
from botocore.client import Config

AWS_ACCESS_KEY_ID = 'admin'
AWS_SECRET_ACCESS_KEY = 'lightningdb123'
AWS_BUCKET_PREFIX = ''
ENDPOINT_URL = 'https://minio.k8s.lightningdb:443'



def datacatalog_list_existing_buckets(request):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, endpoint_url=ENDPOINT_URL, verify=False)
    bucket_list = s3.list_buckets()
    result='['
    for bucket in bucket_list['Buckets']:
        if len(result) > 1:
            result = result + ','
        result = result + ' {"Name":"' +  bucket["Name"] + '"}'
    result = result + ']'
    return HttpResponse(result)


def datacatalog_list_bucket(request, bucket):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, endpoint_url=ENDPOINT_URL, verify=False)
    obj_list = s3.list_objects(Bucket=bucket)
    contents_list = obj_list['Contents']
    result='['
    for content in contents_list:
        if len(result) > 1:
            result = result + ','
        content['LastModified'] = content['LastModified'].strftime("%Y-%m-%d %H:%M:%S%z (%Z)")
        result = result + ' ' + json.dumps(content) 
    result = result + ']'
    return HttpResponse(result)

def datacatalog_list_bucket_es(request, bucket):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, endpoint_url=ENDPOINT_URL, verify=False)
    obj_list = s3.list_objects(Bucket=bucket)
    contents_list = obj_list['Contents']
    result=''
    id = 0
    for content in contents_list:
        id += 1
        idx_string = '{"index":{"_id": "' + str(id) + '"}}\n'
        result = result + idx_string 
        content['LastModified'] = content['LastModified'].strftime("%Y-%m-%d %H:%M:%S%z (%Z)")
        result = result + json.dumps(content) + '\n' 
    return HttpResponse(result)

