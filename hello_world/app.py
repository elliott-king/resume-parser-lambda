import json
import boto3
import pprint

# import requests

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    try:
        response = s3.get_object(Bucket=BUCKET, Key=KEY)
        print('CONTENT TYPE:', response['ContentType'])
        print('response:')
        pprint.pprint(response)
        print('event')
        pprint.pprint(event)
        print('payload')
        pprint.pprint(event.get('payload'))
        # return json.loads(json.dumps(response, default=str))
        # defined by https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format
        return {
            'statusCode': 200,
            'isBase64Encoded': False,
            'body': json.dumps(response, default=str)
        }
        # return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(KEY, BUCKET))
        raise e