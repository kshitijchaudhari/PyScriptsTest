import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)

ec3 = boto3.resource('ec2')
instance = ec3.create_instances(
    ImageId = 'ami-009d6802948d06e52',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'SampleNEW')
print (instance[0].id)