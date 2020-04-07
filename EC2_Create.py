import boto3

session = boto3.Session(profile_name='default')
client = boto3.client('ec2')


def cretae_EC2(AMI,InstanceType,KeyPair):
    response = client.run_instances(
            ImageId=AMI,
            InstanceType=InstanceType,
            MaxCount=1,
            MinCount=1,
            KeyName=KeyPair,
            TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                                {
                                  'Key': 'Project',
                                  'Value': 'Test'
                                },
                                {
                                  'Key': 'Name',
                                  'Value': 'Test Server'
                                },
                            ]
                    }
                    ]
    )

cretae_EC2('ami-0fc61db8544a617ed','t2.micro','dextertest')
