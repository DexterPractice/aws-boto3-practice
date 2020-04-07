import boto3

session = boto3.Session(profile_name='default')
client = boto3.client('ec2')
ec2 = session.resource('ec2')


def create_EC2(AMI,InstanceType,KeyPair):
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

create_EC2('ami-0fc61db8544a617ed','t2.micro','dextertest')

def EC2_list():
    instances = ec2.instances.all()
    for instance in instances:
        print(', '.join((
        instance.id,
        instance.instance_type,
        instance.placement['AvailabilityZone'],
        instance.state['Name']
        )))

EC2_list()
