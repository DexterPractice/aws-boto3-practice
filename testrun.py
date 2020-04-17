import boto3

session = boto3.Session(profile_name='default')

account_id = boto3.client('sts').get_caller_identity().get('Account')
ec2 = boto3.client('ec2')

regions = [region['RegionName']
        for region in ec2.describe_regions()['Regions']]

for region in regions:
    print("Region:", region)
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_snapshots(OwnerIds=[account_id])
    snapshots = response["Snapshots"]
    snapshots.sort(key=lambda x: x["StartTime"])
    snapshots = snapshots[:-1]

    for snapshot in snapshots:
            id = snapshot['SnapshotId']
            try:
                print("Deleting snapshot:", id)
                ec2.delete_snapshot(SnapshotId=id)
            except Exception as e:
                print("Snapshot {} in use, skipping.".format(id))
                continue
