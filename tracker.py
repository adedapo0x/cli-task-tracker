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
            return 1
        last_line = None
        with open(self.filename, 'rb') as file:
            file.seek(0, 2)
            fileSize = file.tell()

            if fileSize == 0:
                return 1
            for i in range(fileSize -1, fileSize - 4, -1):
                file.seek(i)
                character = file.read(1)

                if character == b'\n' and i != fileSize-1:
                    last_line = file.readline().decode().strip()
            else:
                file.seek(0)
                last_line = file.readline().decode().strip()
            last_object = json.loads(last_line)
            return last_object.get(id, 1)
        return 1

    def addToFile(self, data):
        lastId = self.getLastId
        inputted_data = {"id": lastId + 1,
                "description": data,
                "status": "toDo",
                "createdAt": datetime.now(timezone.utc),
                "updatedAt": None
            }
        with open(self.filename, 'a') as file:
            json.loads(inputted_data)
            file.write('\n')
        
record = FileManager('record.jsonl')


while not finished:
    input_command = input()
    splitted_input = input_command.split() 
    
    if splitted_input[0] == "add":
        record.addToFile()
    
    finished = True




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




