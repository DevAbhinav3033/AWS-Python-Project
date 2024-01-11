import json
import boto3

sqs = boto3.client('sqs')
response = sqs.create_queue(
    QueueName='my-queue'
)
queue_url = response['QueueUrl']


def hello(event, context):
    try:

        response=sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=(json.dumps(event))
        )
        print (f"Message successfully sent, Message Id : {response['MessageId']}")
        return {
            "statusCode" : 200 ,
            "body" : json.dumps(response)
        }
    except Exception as e:
        print (e)
        return {
            'statusCode': 500,
            "body": "Error occured in execution of lambda"

        }
    
