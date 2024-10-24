import json, os
from datetime import datetime

class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.lastId = self.getLastId()

    def getLastId(self):
        if not os.path.exists(self.filename):
            return 0
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                fileSize = os.path.getsize(self.filename)
                if fileSize == 0: # if file is empty
                    return 0 
                last_line = [line.strip() for line in file if line.strip()][-1]
                last_object = json.loads(last_line)
                return last_object.get("id", 0)
        except Exception as err:
                print(f"Failed to parse, {err}")

    def addToFile(self, data):
        lastId = self.getLastId()
        inputted_data = {"id": lastId + 1,
                "description": data,
                "status": "toDo",
                "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updatedAt": None
            }
        
        try:
            with open(self.filename, 'a') as file:
                json_str = json.dumps(inputted_data)
                file.write(json_str + '\n')
                print(f"Task added successfully (ID: {lastId + 1})")
        except Exception as e:
            print(f"Failed to append to file, {e}")


    def updateTask(self, inputID, update):
        if not os.path.exists(self.filename):
                print("No task available in tracker!")
                return

        with open(self.filename, 'r') as file:
            file_list = file.readlines()

            if int(inputID) < 1 or int(inputID) > len(file_list):
                print("Task ID not in tracker!")
                print("To view tasks and their IDs, enter 'list'")
                return

        task_json = file_list[int(inputID) - 1]

        # updates particular task description 
        task = json.loads(task_json)
        task["description"] = update
        task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # prepare data to write back to file
        file_list[int(inputID) - 1] = json.dumps(task) + '\n'

        with open(self.filename, 'w') as file:
            file.writelines(file_list)

        print(f"Task updated successfully! (ID: {inputID})")

    def deleteTask(self, inputID):
        if not os.path.exists(self.filename):
                print("No task available in tracker!")
                return
        data = []
        with open(self.filename, 'r') as file:
            for line in file:
                data.append(json.loads(line.strip()))
        

        if int(inputID) < 1 or int(inputID) > len(data):
            print("Task ID not in tracker!")
            print("To view tasks and their IDs, enter 'list'")
            return
        
        data = [obj for obj in data if obj["id"] != int(inputID)]

        for i, obj in enumerate(data,start=1):
            obj["id"] = i
        
        with open(self.filename, 'w') as file:
            for obj in data:
                json_str = json.dumps(obj)
                file.write(json_str + '\n')

        print("Delete operation successful")






