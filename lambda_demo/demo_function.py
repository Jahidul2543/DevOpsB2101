import boto3
import json
import logging
import lambda_demo.base


"""
What is boto3?
Why should we use this?

"""
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2021-07-16T00:46:21.929Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAZWOJ3UI3T2NMPAIMA'}, 'requestParameters': {'sourceIPAddress': '68.132.88.146'}, 'responseElements': {'x-amz-request-id': 'CHQ98QSD6ZR7AJJ5', 'x-amz-id-2': 'Inel8jYmKBpKa/Mx9+kh8QWU4ypcf2qQ2O2vfkhFwq1Zt4Y5p9pdgBm6qosm1KFrEPAoM++pyK8Abk2zpWTfEx7iKl7Y4C8o'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'new-file', 'bucket': {'name': 'izaanit-b2101-2', 'ownerIdentity': {'principalId': 'AF4ZHGIO0PPM9'}, 'arn': 'arn:aws:s3:::izaanit-b2101-2'}, 'object': {'key': '21.jpeg', 'size': 335043, 'eTag': 'ed5d21424126e9bdfbc08af5a5252933', 'sequencer': '0060F0D6E4C544E49D'}}}]}


def lambda_handler(event, context):
    logger.info('got event{}'.format(event))
    logger.error('something went wrong')
    logger.info('Invoked Funtion ARN: {}'.format(context.invoked_function_arn))
    # bucket_list = list_buckets()
    object_url = build_s3_object_url(event)
    pre_signed_url = lambda_demo.base.create_presigned_url()
    send_email(object_url)

    return {
        "bucketsList" : object_url
    }


def list_buckets():
    bucket_list = []
    response = s3_client.list_buckets()['Buckets']
    total_buckets = len(response)

    for i in range(total_buckets):
        bucket_name = s3_client.list_buckets()['Buckets'][i]['Name']
        if bucket_name == 'aws-codestar-us-east-1-666680140343-demo-b2002-pipe':
            # Notify via email
            send_email(bucket_name)
        bucket_list.append(bucket_name)

    logger.info('Bucket List: {}'.format(bucket_list))
    # print(len(bucket_list))
    return bucket_list
    # print(json.loads(response.text))
    # print(type(response))
    # print(response)
    # pprint(response)
    # list_of_buckets = response


def send_email(info):
    response = ses_client.send_email(
        Source='jahidul2543@gmail.com',
        Destination={
            'ToAddresses': [
                'testdata.islam@gmail.com',
            ]
        },
        Message={
            'Subject': {
                'Data': 'Resume Link ' + info,
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': 'This is a test email',
                    'Charset': 'utf-8'
                }
            }
        }
    )
    logger.info('Email response {}'.format(response))


def build_s3_object_url(event):
    bucket_name = event.get('Records')[0].get('s3').get('bucket').get('name')
    object_key = event.get('Records')[0].get('s3').get('object').get('key')
    object_url = 'https://' + bucket_name + '.s3.amazonaws.com/' + object_key
    return object_url




# r = list_buckets()
# print(r)

