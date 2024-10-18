import json
import os
from datetime import datetime, timezone

print("Welcome to Task-Tracker!!")
print("Use commands 'add', 'remove' and co to use the application, press 'help' to get more information")

finished = False

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.lastId = self.getLastId()

    def getLastId(self):
        if not os.path.exists(self.filename):
            return 0
        line = ''
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                fileSize = os.path.getsize(self.filename)

                if fileSize == 0:
                    return 0
                for line in file:
                    pass
                last_line = line.strip()
                last_object = json.loads(last_line)
                return last_object.get("id", 0)
        except Exception as err:
                print(f"Failed to parse, {err}")

    def addToFile(self, data):
        lastId = self.getLastId()
        print(lastId)
        inputted_data = {"id": lastId + 1,
                "description": data,
                "status": "toDo",
                "createdAt": datetime.now(timezone.utc).isoformat(),
                "updatedAt": None
            }
        try:
            with open(self.filename, 'a') as file:
                json_str = json.dumps(inputted_data)
                file.write(json_str + '\n')
        except Exception as e:
            print(f"Failed to append to file, {e}")

record = FileManager('record.jsonl')


while not finished:
    input_command = input()
    splitted_input = input_command.split() 
    task = ' '.join(splitted_input[1:])
    
    if splitted_input[0] == "add":
        record.addToFile(task)
    
    




# parser = argparse.ArgumentParser() 

# parser.add_argument('command')
# parser.add_argument('ID', nargs='?')
# parser.add_argument('task', nargs='?')

# args = parser.parse_args()

# command = args.command.lower()
# id = args.ID if args.ID else None
# task = args.task if args.task else None

# stop = False
# while True:
#     total_input = input()



# now = datetime.now(timezone.utc)

# # if command == "add":
# #     ...



# current_task = {"id": id, "command": command, "id": id, "task": task }

# inputted_task = { "id", "description", "status", "createdAt","updatedAt"}

# with open('record.json', 'a') as record:
#     record.write(json.dumps(current_task) + "\n")




