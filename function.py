import json
import csv
import requests


def lambda_handler(event, context):
    url = 'https: // firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Global_24h.csv'
    data = requests.get(url)

    print('-=' * 40)
    print(data)
    print('-=' * 40)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
