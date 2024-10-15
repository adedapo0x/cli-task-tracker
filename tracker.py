import argparse

parser = argparse.ArgumentParser()

parser.add_argument('command')

args = parser.parse_args()

command = str(args.command).lower()



