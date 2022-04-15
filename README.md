# data_catalog_django

## Install
```
// python3
python3 -m venv venv-python3
source venv-python3/bin/activate

// python django server
django-admin startproject dc   // project start
python manage.py migrate  // sqlite3 사용
nohup python manage.py runserver 0.0.0.0:8000 > log.out 2>&1 &  // runserver
tail -f log.out

python manage.py startapp datacatalog     // app start

// modified
/dc/dc/settings.py
/dc/dc/urls.py
/dc/datacatalog/views.py

```


## How to use

### file list-up

```
curl -X GET "http://{hostname}:8000/data_catalog/list/"
```

- example
```
$ curl -X GET "http://fbg04:8000/data_catalog/list/" | jq .
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
```

### file upload


### file search


