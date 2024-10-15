import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('command')
parser.add_argument('ID', nargs='?', default=1)
parser.add_argument('task')

args = parser.parse_args()

command = args.command.lower()
id = args.ID
task = args.task

current_task = [command, id, task]

with open('record.json', 'a') as record:
    json.dump(current_task, record)




