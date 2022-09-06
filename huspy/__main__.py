import sys
import argparse
import huspy

def build_parser():
    """
      Constructs the parser for the command line arguments.
      Returns:
        An ArgumentParser instance for the CLI.
    """
    parser = argparse.ArgumentParser(prog='huspy', description='Formatter for Python code.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(huspy.__version__))
    parser.add_argument('--install', action='store_true', help='install githook')
    parser.add_argument('--uninstall', action='store_true', help='install githook')
    parser.add_argument('--set', type=str, nargs=2, help='set githook')
    parser.add_argument('--add', type=str, nargs=2, help='add githook')
    return parser


def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv[1:])

    if args.install:
        huspy.install()
    elif args.uninstall:
        huspy.uninstall()
    elif args.set:
        huspy.set(args.set[0], args.set[1])
    elif args.add:
        huspy.add(args.add[0], args.add[1])
    pass


if __name__ == '__main__':
    sys.exit(main(sys.argv))