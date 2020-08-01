from awsresources.ami import AmiAnalyzer
from awsresources.securitygroup import SgAnalyzer
from awsresources.elasticip import ElasticIpAnalyzer

from core.argument_parser import CliArgumentParser
from core.log import Logging

class Analyzer(Logging):
    def __init__(self):
        self.log = Logging()

    def aws_scan(self, args):
        if args.ami and args.owner:
            return AmiAnalyzer().find_public_ami(owners=[args.owner])

        if args.sg:
            if args.cidr:
                return SgAnalyzer(args.cidr).find_security_group_by_rule()

            return SgAnalyzer().find_security_group_by_rule()

        if args.elasticip:
            return ElasticIpAnalyzer().find_elastic_dissociated()
