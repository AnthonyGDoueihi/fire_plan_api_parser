import json
import csv
import requests
import io
import datetime


def lambda_handler(event, context):
    now = datetime.datetime.now()
    url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_Global_24h.csv'
    response = requests.get(url)
    reader = csv.DictReader(io.StringIO(response.text))
    for row in reader:
        if (now - datetime.timedelta(hours=12)) < (datetime.datetime(int(row['acq_date'][0:4:]), int(row['acq_date'][5:7:]), int(row['acq_date'][8:10:]), int(
            row['acq_time'][0:2:]), int(row['acq_time'][2:4:]))):
            print(row)
            break

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
