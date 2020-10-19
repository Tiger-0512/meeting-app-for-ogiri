# function for rest api which gets data from dynamoDB
# coding: utf-8

# ①ライブラリのimport
import datetime
import decimal
import boto3
from boto3.dynamodb.conditions import Key, Attr

import random
import time

# ②Functionのロードをログに出力
# print('Loading function')

# ③DynamoDBオブジェクトを取得
dynamodb = boto3.resource('dynamodb')

# ④Lambdaのメイン関数
def lambda_handler(event, context):
    num = random_num(50)
    
    # ⑤テーブル名を指定
    table_name = "smmi-ogiri-tbl"
    
    # ⑥参照データのキーの設定
    # partition_key = {"Id": event["Id"]}
    partition_key = {"Id": num}

    # ⑦DynamoDBテーブルのオブジェクトを取得
    dynamotable = dynamodb.Table(table_name)

    # ⑧データの読み取り
    res = dynamotable.get_item(Key=partition_key)
    item = res["Item"]
    
    return item

def random_num(last):
    num = random.randint(1, last)
    if 0 < num < 10:
        num = '0' + str(num)
    else:
        num = str(num)
    return (num)