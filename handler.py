import json
import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/054244991161/aws-python-project-dev-my-queue'



def hello(event, context):
    
    response=sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(json.dumps(event))
    )

    return {
        "statusCode" : 200 ,
        "body" : json.dumps(response)
    }

    
