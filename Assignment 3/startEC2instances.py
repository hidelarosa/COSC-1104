# COSC 1104 – Assignment 3
# Harlan Dela Rosa
# DEC 4, 2024
# Start EC2 instance using boto3

import boto3

client = boto3.client('ec2', aws_access_key_id='YOUR_ACCESS_KEY',
                      aws_secret_access_key='YOUR_SECRET_ACCESS_KEY', region_name='us-east-1')

response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Dev']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }
    ]
)

ids = [
    instance['InstanceId']
    for reservation in response['Reservations']
    for instance in reservation['Instances']
]

# Start the stopped instances
response = client.stop_instances(
    InstanceIds=ids
)

print("Stopped now", response)

#This script only start all stopped EC2 instances that are for DEV
#Reference https://medium.com/@jasonceballos/stop-all-ec2-instances-with-python-script-ef284e50382d
