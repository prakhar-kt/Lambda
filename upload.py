# define function to upload a file to s3

import boto3


def get_client():
    """Gets the s3 client for AWS"""
    return boto3.client('s3')


def upload_s3(bucket, file, body):
    """Uploads a file to S3 bucket"""
    # get the s3 boto3 client
    s3_client = get_client()

    # upload the file to the s3 bucket
    res = s3_client.put_object(
        Bucket=bucket,
        Key=file,
        Body=body
    )

    return res