import json

def lambda_handler(event, context):
    # Event contains the WebSocket message payload
    body = event.get("body", "{}")
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Vote received successfully",
            "payload": body
        })
    }
