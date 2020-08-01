import boto3
from core.log import Logging


class AmiAnalyzer(Logging):
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.log = Logging()


    def find_public_ami(self, owners):
        amis = self.ec2.describe_images(
            Owners=owners
        )

        for ami in amis['Images']:
            ami_id = ami['ImageId']

            if ami['Public']:
                self.log.print_yellow("[+] AMI with ID {0} is public!".format(ami_id))
