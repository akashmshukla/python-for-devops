'''
Install boto3:
pip install boto3
---------------------------------
Install AWS CLI:
---------------------------------
Configure AWS Credentials:
aws configure
---------------------------------
List S3 Buckets:
import boto3

# Create S3 client
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()

print("S3 Buckets:")
for bucket in response['Buckets']:
    print(bucket['Name'])
'''