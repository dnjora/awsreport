from core.ami import AmiAnalyzer
from core.argument_parser import CliArgumentParser

def main():
    parser = CliArgumentParser()
    args = parser.argument_parser()

    if args.ami:
        ami = AmiAnalyzer().find_public_ami(owners=[args.owner])

if __name__=='__main__':
    main()
