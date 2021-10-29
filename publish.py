# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import random
from datetime import datetime

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "a2bd803uieoupu-ats.iot.ap-south-1.amazonaws.com"
CLIENT_ID = "Edge"
PATH_TO_CERT = "./aws/device-certificate.pem.crt"
PATH_TO_KEY = "./aws/private.pem.key"
PATH_TO_ROOT = "./aws/AmazonRootCA1.pem"
MESSAGE = "Hello World"
TOPIC = "Edge/publish"
RANGE = 20

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 443)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

myAWSIoTMQTTClient.connect()
print('Begin Publish')
for i in range (RANGE):
    message = {}
    message['LV ActivePower (kW)'] = random.uniform(300,1200)
    message['Wind Speed (m/s)'] = random.uniform(4,13)
    message['Wind Direction (°)'] = random.uniform(30,400)
    message['Temperature'] = random.uniform(-50,80) 
    message['severity'] = 0
    if message['Temperature'] > -20 and message['Temperature'] < 50:
        message['severity'] = 0
    else:
        message['severity'] = 1 
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'Edge/publish'")
    t.sleep(1)
print('Publish End')
myAWSIoTMQTTClient.disconnect()