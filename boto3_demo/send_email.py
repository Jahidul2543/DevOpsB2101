import boto3
import json
from pprint import pprint


"""
What is boto3?
Why should we use this?

"""
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')


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


    print(bucket_list)
    print(len(bucket_list))
    #print(json.loads(response.text))
    # print(type(response))
    # print(response)
    # pprint(response)
    # list_of_buckets = response


def send_email(bucket_name):
    response = ses_client.send_email(
        Source='jahidul2543@gmail.com',
        Destination={
            'ToAddresses': [
                'it.abtraining@gmail.com',
            ]
        },
        Message={
            'Subject': {
                'Data': 'Bucket ' + bucket_name + 'found' ,
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
    print('email response {}'.format(response))


list_buckets()

