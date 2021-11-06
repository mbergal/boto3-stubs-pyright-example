import boto3
from mypy_boto3_s3 import S3ServiceResource

s3_client = boto3.client("s3")
s3_resource: S3ServiceResource = boto3.resource("s3")
