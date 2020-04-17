import boto3

session = boto3.Session(profile_name='default')

ec2 = boto3.client('ec2')

regions = [region['RegionName']
        for region in ec2.describe_regions()['Regions']]

for region in regions:
    print("Region:", region)
    ec2 = boto3.resource('ec2', region_name=region)

    volumes = ec2.volumes.filter(
        Filters=[{'Name': 'status', 'Values': ['available']}])
    for volume in volumes:
        v = ec2.Volume(volume.id)
        print("Deleting EBS volume: {}, Size: {} GiB".format(v.id, v.size))
        v.delete()
