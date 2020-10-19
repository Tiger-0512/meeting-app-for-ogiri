# function for websocket api to get problems from dynamoDB with real-time communication

# If you use this function,
# 1. You install 'requests' module in local.  $ pip install requests -t .
# 2. Zip the function and modules.
# 3. Upload to lambda function in aws console.


# -*- coding: utf-8 -*-

import json
import os
import sys
import logging
import boto3
import botocore
from botocore.exceptions import ClientError

import requests

dynamodb = boto3.resource('dynamodb')
connections = dynamodb.Table(os.environ['CONNECTION_TABLE'])

def lambda_handler(event, context):
    post_data = requests.post('https://lhaj6ye9la.execute-api.ap-northeast-1.amazonaws.com/getDataAPI/dynamodb-ctrl')
    pbm = json.loads(post_data.content)['Problem']
    # pbm = pbm.encode('utf-8')
    # pbm = pbm.decode('unicode-escape')
    print(pbm)
    
    print(event)
    domain_name = event.get('requestContext',{}).get('domainName')
    stage       = event.get('requestContext',{}).get('stage')
    
    items = connections.scan(ProjectionExpression='Id').get('Items')
    print(items)
    if items is None:
        return { 'statusCode': 500,'body': 'something went wrong' }
    
    apigw_management = boto3.client('apigatewaymanagementapi',
                                    endpoint_url="https://" + domain_name + "/" + stage)
    
    print(apigw_management)
    
    #post_data = json.loads(event.get('body', '{}')).get('data')

    body = {'message': 'ok'}
    body_json = json.dumps(body)
    
    for item in items:
        try:
            print(item)
            apigw_management.post_to_connection(ConnectionId=item['Id'],
                                                        Data=json.dumps(pbm))
        except ClientError as e:
            print(e)
    return { 'statusCode': 200,'body': body_json }