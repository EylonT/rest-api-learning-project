import boto3
import pandas as pd
import yaml

# Get the service resource
sqs = boto3.client('sqs')
s3 = boto3.resource('s3')

# Get the queue
queue = sqs.receive_message(QueueUrl='data_pipeline', MaxNumberOfMessages=10, VisibilityTimeout=20)
messages = queue.get('Messages')
data_dict = {}

# Write the messages to a file and upload them to S3
try:
    for message in messages:
        data_dict = yaml.safe_load(message.get('Body'))
        data_dict.update(data_dict)
        message = queue['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl='data_pipeline',
            ReceiptHandle=receipt_handle
            )
        print('Received and deleted message: %s' % message)
    pd.DataFrame.from_dict(data_dict, orient='index').to_csv(r'./products.csv', mode='a')
    s3.meta.client.upload_file('./products.csv', '<change-me>', 'products.csv')

except TypeError:
    pass

except Exception as e:
    print(e)