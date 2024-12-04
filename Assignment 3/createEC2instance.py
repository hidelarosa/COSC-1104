# COSC 1104 – Assignment 3
# Harlan Dela Rosa
# DEC 4, 2024
# Creating EC2 instance using boto3

import boto3

# Create an AWS session
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='us-east-1'
)

ec2_resource = session.resource('ec2')


instances = ec2_resource.create_instances(
    ImageId='ami-0c55b159cbfafe1f0',  
    MinCount=1,
    MaxCount=5,
    InstanceType='t2.micro',
    KeyName='vockey',  
    SecurityGroupIds=['sg-0721d96d77c622094'], # default security group in AWS that allows HTTP and SSH Access.
    SubnetId='subnet-0bd4110961d1e5b8f',   # default AWS subnet ID 
    TagSpecifications=[
        {
            'ResourceType': 'instance',  # tags to specify the purpose of this EC2 instance
            'Tags': [
                {
                    'Key': 'Environment',
                    'Value': 'Dev'
                },
            ]
        },
    ]
)


#reference https://www.tutorialspoint.com/launching-aws-ec2-instance-using-python
# I've added Secu