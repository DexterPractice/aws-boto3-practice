import os
import tempfile

import boto3


s3 = boto3.client('s3')
DEST_BUCKET = "https://s3.console.aws.amazon.com/s3/buckets/dextertest-dest-image"
SIZE = 128, 128

def lambda_handler(event, context):

    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        thumb = 'thumb-' + key
        with tempfile.TemporaryDirectory() as tmpdir:
            download_path = os.path.join(tmpdir, key)
            upload_path = os.path.join(tmpdir, thumb)
            s3.download_file(source_bucket, key, download_path)
            generate_thumbnail(download_path, upload_path)
            s3.upload_file(upload_path, DEST_BUCKET, thumb)

        print('Thumbnail image saved at {}/{}'.format(DEST_BUCKET, thumb))
