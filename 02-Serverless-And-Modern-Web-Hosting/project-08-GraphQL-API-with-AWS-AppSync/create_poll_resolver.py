import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PollsTable')

def lambda_handler(event, context):
    args = event['arguments']

    item = {
        'id': args['id'],
        'question': args['question'],
        'options': args['options']
    }

    table.put_item(Item=item)

    return item
