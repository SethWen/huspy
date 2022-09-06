import sys
import argparse
from huspy import cli

def build_parser():
    """
      Constructs the parser for the command line arguments.
      Returns:
        An ArgumentParser instance for the CLI.
    """
    parser = argparse.ArgumentParser(prog='huspy', description='Formatter for Python code.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(cli.__version__))
    parser.add_argument('--install', action='store_true', help='install githook')
    parser.add_argument('--uninstall', action='store_true', help='install githook')
    parser.add_argument('--set', type=str, nargs=2, help='set githook')
    parser.add_argument('--add', type=str, nargs=2, help='add githook')
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args(sys.argv[1:])

    if args.install:
        cli.install()
    elif args.uninstall:
        cli.uninstall()
    elif args.set:
        cli.set(args.set[0], args.set[1])
    elif args.add:
        cli.add(args.add[0], args.add[1])
    pass


if __name__ == '__main__':
    sys.exit(main())