import boto3

session = boto3.Session(profile_name='default')
ec2 = boto3.resource('ec2')

def list_volumes():
    instances = ec2.instances.all()
    for i in instances:
        for v in i.volumes.all():
            print(", ".join((
                v.id,
                i.id,
                v.state,
                str(v.size) + "GiB",
                v.encrypted and "Encrypted" or "Not Encrypted"
            )))
            return
print(list_volumes())
