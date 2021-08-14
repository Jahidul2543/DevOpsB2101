import boto3, json, logging
from pprint import pprint

client = boto3.client('s3')
ses_client = boto3.client('ses')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    r = get_bucket_list()
    #pprint('Bucket_List: {}'.format(r))
    return {
        'statusCode': 200,
        'body': r
    }


def get_bucket_list():
    response = client.list_buckets()
    # pprint(response)
    # logger.info(response)
    bucket_list = []
    for i in response['Buckets']:
        bucket_name = i['Name']
        bucket_list.append(bucket_name)

    return bucket_list


# python-lambda-local -f lambda_handler -t 30 get_s3_list.py event.json

