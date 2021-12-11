from flask import Flask, request, jsonify
import boto3

# Initialize the flask app
app = Flask(__name__)

# Create the /api route and allow the client to POST json
@app.route('/api', methods=['POST'])
def post_request():
    products = request.get_json()
    if products is None:
        return '400 Message is required'

# Try to send the message from the client to the sqs queue
    try:
        sqs = boto3.resource('sqs')
        queue = sqs.get_queue_by_name(QueueName='data_pipeline')
        response = queue.send_message(MessageBody=str(products))
        return '200 Message sent'

    except Exception as e:
        print(e)
        return "500 either you don't have permissions, credential issues, or queue doesn't exist, check server for errors"

if __name__ == '__main__':
    app.run(host='0.0.0.0')