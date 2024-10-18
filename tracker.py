import json
import os
from datetime import datetime, timezone
from class_definition import FileManager

print("Welcome to Task-Tracker!!")
print("Use commands 'add', 'remove' and co to use the application, press 'help' to get more information")

finished = False

record = FileManager('record.jsonl')

while not finished:
    input_command = input()
    splitted_input = input_command.split() 
    task = ' '.join(splitted_input[1:])
    
    if splitted_input[0] == "add":
        record.addToFile(task)

    elif splitted_input[0] == "end":
        finished = True
    
    








