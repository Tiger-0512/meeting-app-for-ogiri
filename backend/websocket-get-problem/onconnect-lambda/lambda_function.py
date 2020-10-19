# onconnect function for websocket api

import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
connections = dynamodb.Table(os.environ['CONNECTION_TABLE'])

def lambda_handler(event, context):
    print(event)
    connection_id = event.get('requestContext',{}).get('connectionId')
    print(connection_id)

    body = {'message': 'ok'}
    body_json = json.dumps(body)

    result = connections.put_item(Item={ 'Id': connection_id })
    return { 'statusCode': 200,'body': body_json }
