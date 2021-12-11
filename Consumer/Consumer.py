import boto3
import pandas as pd
import yaml
import json

# Get the service resource
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')

# Get the queue
queue = sqs.receive_message(QueueUrl='data_pipeline', MaxNumberOfMessages=10, VisibilityTimeout=20)
messages = queue.get('Messages')
data_dict = {} # Create empty dictionary to store all the queue messages

# Write the messages to a file and upload them to S3
try:
    for message in messages:
        data_dict = yaml.safe_load(message.get('Body')) # Get the message body and turn it from string to dict
        data_dict.update(data_dict) #  Insert the message body to the outer dict data_dict
        message = queue['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl='data_pipeline',
            ReceiptHandle=receipt_handle
            )
        print('Received and deleted message: %s' % message)
        data = pd.json_normalize(data_dict) # Flatten the json to a flat table.
        data.to_csv(r'./products.csv', mode='a') # Write the data to a csv file
        s3.meta.client.upload_file('./products.csv', '<change-me>', 'products.csv') # Upload the csv to S3

except TypeError:
    pass

except Exception as e:
    print(e)