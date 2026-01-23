import json
import boto3

sns = boto3.client('sns')

# Replace with your actual SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:191280371533:event-driven-topic"

def lambda_handler(event, context):
    message = {
        "eventType": "ORDER_CREATED",
        "orderId": "ORD-1001",
        "status": "CREATED"
    }

    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=json.dumps(message)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Event published successfully",
            "messageId": response["MessageId"]
        })
    }

