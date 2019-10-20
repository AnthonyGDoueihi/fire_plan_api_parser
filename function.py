import json
import csv
import requests
import io
import datetime
from math import sin, cos, sqrt, atan2, radians
import boto3

def get_distance_from_latLng(lat1, lat2, lng1, lng2):
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lng1 = radians(lng1)
    lng2 = radians(lng2)
    deltaLat = lat1 - lat2
    deltaLng = lng1 - lng2

    a = sin(deltaLat / 2)**2 + cos(lat1) * \
        cos(lat2) * sin(deltaLng / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def lambda_handler(event, context):
    '''
    now = datetime.datetime.now()
    url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Global_24h.csv'
    response = requests.get(url)
    reader = csv.DictReader(io.StringIO(response.text))
    for row in reader:
        if (now - datetime.timedelta(hours=12)) < (datetime.datetime(int(row['acq_date'][0:4:]), int(row['acq_date'][5:7:]), int(row['acq_date'][8:10:]), int(
            row['acq_time'][0:2:]), int(row['acq_time'][2:4:]))):
            distance = get_distance_from_latLng(1, float(row['latitude']), -50, float(row['longitude']))
            print(distance)
            break
    '''
    
    dynamodb = boto3.client('dynamodb')

    items = dynamodb.scan(TableName='FireActionUser',
        IndexName='id-index',
        Select='ALL_ATTRIBUTES')

    print(f'Response is HERE: {items}')

    return {
        'statusCode': 200,
        'body': 'Yay'
    }