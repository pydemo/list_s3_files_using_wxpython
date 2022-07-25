import boto3
from botocore import UNSIGNED
from botocore.client import Config
from pprint import pprint as pp

s3pub = boto3.client('s3')
resp = s3pub.list_objects_v2(Bucket='test', Prefix='test/path',MaxKeys=10 )
pp(len(resp['Contents']))
pp(resp['Contents'])