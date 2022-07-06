import json, os
from download import download_file
from upload import upload_s3
from util import get_prev_file_name, \
    get_next_filename, upload_bookmark




def lambda_handler(event, context):

    environ = os.environ.get('ENVIRON')
    if environ == 'DEV':
        print(f"Running in {environ} environment")
        os.environ.setdefault('AWS_PROFILE','data_engineer')

    bucket_name = os.environ.get('BUCKET_NAME')
    bookmark_file = os.environ.get('BOOKMARK_FILE')
    baseline_file = os.environ.get('BASELINE_FILE')
    file_prefix = os.environ.get('FILE_PREFIX')

    while True:

        prev_filename = get_prev_file_name(bucket_name, file_prefix, bookmark_file, baseline_file)
        file_name = get_next_filename(prev_filename)

        download_res = download_file(file_name)

        if download_res.status_code == 404:
            print(f'Invalid file name or downloads caught up till {prev_filename}')
            break

        upload_res = upload_s3(
            bucket_name,
            f"{file_prefix}/{file_name}",
            download_res.content

        )

        print(f'File {file_name} successfully processed')
        upload_bookmark(bucket_name, file_prefix, bookmark_file, file_name)
    return upload_res
