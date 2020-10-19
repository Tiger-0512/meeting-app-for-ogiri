# disconnect function for websocket-api

import json
import os
import logging
import boto3

dynamodb = boto3.resource('dynamodb')
connections = dynamodb.Table(os.environ['CONNECTION_TABLE'])


def lambda_handler(event, context):
    connection_id = event.get('requestContext',{}).get('connectionId')
    
    body = {'message': 'ok'}
    body_json = json.dumps(body)
    
    result = connections.delete_item(Key={ 'Id': connection_id })
    return { 'statusCode': 200, 'body': body_json }