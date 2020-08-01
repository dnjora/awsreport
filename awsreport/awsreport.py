from core.argument_parser import CliArgumentParser
from core.analyzer import Analyzer

def main():
    parser = CliArgumentParser()
    args = parser.argument_parser()
    analyzer = Analyzer()

    analyzer.aws_scan(args)

if __name__=='__main__':
    main()
