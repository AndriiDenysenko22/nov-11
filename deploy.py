import boto3


def get_ips():
    ec2 = boto3.resource("ec2", region_name="us-east-1")
    filters = [
        {"Name": "tag:project", "Values": ["*nov-11*"]},
        {"Name": "tag:env", "Values": ["*dev*"]},
    ]
    response = ec2.instances.filter(Filters=filters)

    for instance in response:
        print(instance.public_ip_address)


def deploy(ip):
    """
    Go via ssh to machine and deploy it
    """
    print(f'Starting deploy to {ip}')

def do_deploy():
    for ip in get_ips():
        deploy(ip)
