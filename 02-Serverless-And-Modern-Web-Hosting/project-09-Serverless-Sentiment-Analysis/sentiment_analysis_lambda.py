import json
import boto3

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    # API Gateway sends body as string
    body = event.get("body", "{}")

    if isinstance(body, str):
        body = json.loads(body)

    text = body.get("text", "")

    if not text:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No text provided"})
        }

    response = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )

    result = {
        "text": text,
        "sentiment": response["Sentiment"],
        "sentimentScore": response["SentimentScore"]
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
