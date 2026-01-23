import json

def lambda_handler(event, context):
    print("EVENT RECEIVED:", event)

    for record in event['Records']:
        message_body = record['body']
        print("MESSAGE BODY:", message_body)

    return {
        "statusCode": 200,
        "body": json.dumps("Messages processed successfully")
    }
