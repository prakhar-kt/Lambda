import json, os
from download import download_file
from upload import upload_s3




def lambda_handler(event, context):
    file = '2021-01-26-0.json.gz'
    download_res = download_file(file)
    environ = os.environ.get('ENVIRON')
    file_prefix = os.environ.get('FILE_PREFIX')
    if environ == 'DEV':
        os.environ.setdefault('AWS_PROFILE', 'data_engineer')

    bucket = os.environ.get('BUCKET_NAME')


    upload_res = upload_s3(
        bucket,
        f'{file_prefix}/{file}',
        download_res.content

    )
    return upload_res