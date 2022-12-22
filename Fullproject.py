import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='File processor CLI')
    parser.add_argument('--filepath', '-f', help='Path to the file to be processed', required=True)
    parser.add_argument('--output', '-out', help='Filename for output results', required=False)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--medals', '-m', nargs=2, help='Get data on the 10 medalists for a specific country in a' ' specific year')
    group.add_argument('--total', '-t', help='Get data about countries which got at least one medal in specific year')
    group.add_argument('--overall', '-o', nargs='+', help='Get the year for specific countries when they won the'' most medals')
    group.add_argument('--interactive', '-i', help='Interactive mode', action='store_true')

    args = parser.parse_args()

    if not args.filepath:
        parser.print_help()
        sys.exit(1)
    if args.medals:
        task1(args.filepath, args.medals, args.output)
    elif args.total:
        task2(args.filepath, args.total, args.output)
    elif args.overall:
        task3(args.filepath, args.overall, args.output)
    elif args.interactive:
        task4(args.filepath)
