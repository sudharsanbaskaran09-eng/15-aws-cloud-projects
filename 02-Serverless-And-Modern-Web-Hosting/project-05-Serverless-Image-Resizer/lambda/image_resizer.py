import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

DEST_BUCKET = "expense-image-resized-sudharsan"

def lambda_handler(event, context):
    try:
        print("EVENT RECEIVED:", event)

        # Get S3 details
        record = event['Records'][0]
        source_bucket = record['s3']['bucket']['name']
        object_key = urllib.parse.unquote_plus(
            record['s3']['object']['key']
        )

        print(f"Source bucket: {source_bucket}")
        print(f"Object key: {object_key}")

        # Copy image to destination bucket
        copy_source = {
            'Bucket': source_bucket,
            'Key': object_key
        }

        s3.copy_object(
            CopySource=copy_source,
            Bucket=DEST_BUCKET,
            Key=object_key
        )

        print("Image copied successfully")

        return {
            'statusCode': 200,
            'body': json.dumps('Image processed successfully')
        }

    except Exception as e:
        print("ERROR:", str(e))
        raise e

