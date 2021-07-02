import requests
import json
import base
import os


url = 'https://izaan-test.auth.us-east-1.amazoncognito.com/oauth2/token'

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/secrets.json') as json_data:
    secrets = json.load(json_data)
    print(secrets)


def get_token():
    print('Get Token')
    payload = "scope=izaan_test%2Fpost_info&grant_type=client_credentials"
    user_name = secrets['userName']
    password = secrets['password']
    credentials = base.encode_base64(user_name, password)
    headers = {
        "Authorization": "Basic " + credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.request("POST", url=url, data=payload, headers=headers)
    # print(type(response))
    # print(response)
    # print(type(response.text))
    # print()
    response_as_dict = json.loads(response.text)
    print(response_as_dict)
    access_token = response_as_dict['access_token']
    return access_token


def age_group_identifier():
    api_url = "https://5x9m5ed0tj.execute-api.us-east-1.amazonaws.com/test/submit"
    token = "Bearer " + get_token()
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    with open("data/submit_payload.json", "r") as read_file:
        file = json.load(read_file)
    print('Payload: {}'.format(file))

    payload = json.dumps(file)
    response = requests.request("POST", url=api_url, data=payload, headers=headers)
    print(json.loads(response.text))


age_group_identifier()
