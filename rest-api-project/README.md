# This project is for learning purposes only. It creates A local REST API flask producer for sqs and local consumer that sends the data to S3.

## Requirements:

* default aws credentials set on your machine.
* python 3
* docker and docker compose

## Installation steps:

1. Upload the architecture.yaml to cloudformation and choose a S3 bucket name.
2. Navigate to Consumer/Consumer.py and change the bucket name in "change me" section.
3. Run docker-compose up -d
4. Open an API client (postman/curl/custom client app)
5. POST to http://127.0.0.1:5000/api

**NOTE**

Warning!
Do not share the images with others after the build because they contain your access and secret keys.
You can share the project with others and run the docker compose.