import boto3

import config
ACCESS_KEY_ID = config.aws_access_key_id
SECRET_ACCESS_KEY = config.aws_secret_access_key

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id=ACCESS_KEY_ID,
aws_secret_access_key=SECRET_ACCESS_KEY
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

def saveFile():
    

    txt_data = b'This is the content of the file uploaded from python boto3 asdfasdf'

    object = s3.Object('<bucket_name>', 'file_name.txt')

    result = object.put(Body=txt_data)

def readContents():
