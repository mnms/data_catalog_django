# data_catalog_django

## Install
```
// python3
python3 -m venv venv-python3
source venv-python3/bin/activate

// python fastapi server
pip install fastapi
pip install uvicorn[standard]
nohup uvicorn main:app --reload --host=0.0.0.0 --port=8000 > log.out 2>&1 &

```

## Docs page
```
http://{hostname}:8000/docs
```


## How to use

### bucket list-up

```
curl -X GET "http://{hostname}:8000/data_catalog/list/buckets/"
```


```

curl -X GET "http://fbg04:8000/data_catalog/list/buckets/" | jq .
[
  {
    "Name": "ai-hub"
  },
  {
    "Name": "data"
  },
  {
    "Name": "hynix"
  },
  {
    "Name": "testbucket"
  },
  {
    "Name": "welcome"
  }
]
```

### file list-up

```
curl -X GET "http://{hostname}:8000/data_catalog/list/bucket/{bucket name}/"
```

- example
```
$ curl -X GET "http://fbg04:8000/data_catalog/list/bucket/ai-hub/" | jq .
[
  {
    "Key": "002.대용량콘텐츠_sample/라벨링데이터/en_animal_20120303180907_20_554_1021352_12_output_H264_1547.json",
    "LastModified": "2022-04-13 13:02:57.526000+00:00",
    "ETag": "\"e3e3e288612c297865151ad1c74ab301\"",
    "Size": 15845,
    "StorageClass": "STANDARD",
    "Owner": {
      "DisplayName": "minio",
      "ID": "02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4"
    }
  },
  {
    "Key": "002.대용량콘텐츠_sample/라벨링데이터/en_animal_20120310180826_20_554_1021835_12_output_H264_1580.json",
    "LastModified": "2022-04-13 13:01:35.460000+00:00",
    "ETag": "\"e3090de83dcb2faf0fc6f1c0fef08806\"",
    "Size": 21055,
    "StorageClass": "STANDARD",
    "Owner": {
      "DisplayName": "minio",
      "ID": "02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4"
    }
  },
  {
    "Key": "002.대용량콘텐츠_sample/라벨링데이터/en_animal_20120407145421_20_554_1023815_12_output_H264_917.json",
    "LastModified": "2022-04-13 13:03:59.304000+00:00",
    "ETag": "\"e337fee3b2715fd22b1702a80fe1f7ba\"",
...


$ curl -X GET "http://fbg04:8000/data_catalog/list/bucket/data/" | jq .
  {
    "Key": "nyc_taxi/part-00078-47ba515b-aa3b-4c19-b5db-25a212e37338-c000.snappy.parquet",
    "LastModified": "2021-07-06 09:03:52+0000 (UTC)",
    "ETag": "\"0db49162fddd4031769a56ff5c0e6c3c\"",
    "Size": 288032230,
    "StorageClass": "STANDARD",
    "Owner": {
      "DisplayName": "minio",
      "ID": "02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4"
    }
  },
  {
    "Key": "nyc_taxi/part-00079-47ba515b-aa3b-4c19-b5db-25a212e37338-c000.snappy.parquet",
    "LastModified": "2021-07-06 09:03:52+0000 (UTC)",
    "ETag": "\"b037752b8a822d558546571d1c7ce666\"",
    "Size": 275296021,
    "StorageClass": "STANDARD",
    "Owner": {
      "DisplayName": "minio",
      "ID": "02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4"
    }
  }
  ...

```

### file upload


### file search


