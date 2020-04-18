import boto3
import datetime
from dateutil.parser import parse

session = boto3.Session(profile_name='default')



def days_old(date):
    parsed = parse(date).replace(tzinfo=None)
    diff = datetime.datetime.now() - parsed
    return diff.days


print(days_old('2020-04-12'))

ec2_client = boto3.client('ec2')
regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]
print(regions)

for region in regions:
    ec2 = boto3.client('ec2', region_name=region)
    print("Region:", region)

    amis = ec2.describe_images(Owners=['self'])['Images']
    for ami in amis:
        creation_date = ami['CreationDate']
        age_days = days_old(creation_date)
        image_id = ami['ImageId']
        print('ImageId: {}, CreationDate: {} ({} days old)'.format(
            image_id, creation_date, age_days))
        if age_days == 0:

            print('Deleting ImageId:', image_id)
            ec2.deregister_image(ImageId=image_id)
