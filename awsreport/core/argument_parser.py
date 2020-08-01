import argparse

class CliArgumentParser():
    def argument_parser(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--ami', '--images',
                            action="store_true",
                            help='Analyze AWS AMI (Images)',
                            required=False)

        parser.add_argument('--sg', '--securitygroup',
                            action="store_true",
                            help='Analyze security groups',
                            required=False)

        parser.add_argument('--cidr',
                            help='Network cidr',
                            required=False)

        parser.add_argument('--owner', '--imagesowner',
                            help="Set the owner of the AMI's",
                            required=False)

        args = parser.parse_args()

        return args
