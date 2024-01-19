import json
import boto3
import os

from weather import get_weather

sqs = boto3.client('sqs')

queue_url= "https://sqs.us-east-1.amazonaws.com/054244991161/weatherQueue"

def hello(event, context):

    try:

        api_key=os.environ.get('WEATHER_API')
        city="Gurgaon"
        
        # Calling weather api function to fetch weather details
        data=get_weather(api_key,city)   
        print(data)

        # Sending the received data to sqs
        response=sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=(json.dumps(data))
        )

        
        print (f"Message successfully sent, Message Id : {response['MessageId']}")

        # Returning the response from the function
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
    
