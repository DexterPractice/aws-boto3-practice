import boto3

session = boto3.Session(profile_name='default')
ec2 = session.resource('ec2')

instances = ec2.instances.all()
x = list(instances)
print(x)
