import json, os
from datetime import datetime, timezone

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
                print(f"Task added successfully (ID: {lastId + 1})")
        except Exception as e:
            print(f"Failed to append to file, {e}")
    
    def findTask(self, inputID):
         # reads file into memory
        with open(self.filename, 'r') as file:
            file_list = file.readlines()

        l = 0
        r = len(file_list) - 1
        task_index = -1
        while l <= r:
            mid = (r + l) // 2
            try:
                midVal = json.loads(file_list[mid])
                if midVal["id"] > int(inputID):
                    r = mid - 1
                elif midVal["id"] < int(inputID):
                    l = mid + 1
                else: 
                    task_index = mid
                    break
            except Exception as e:
                print(f"Error decoding JSON at line {mid + 1}")
                print(e)
                return
        if task_index == -1:
            print("Task ID not in tracker!")
            print("To view tasks and their IDs, enter 'list'")
            return
        else:
            return task_index


    def updateTask(self, inputID, update):
        if not os.path.exists(self.filename):
                print("No task available in tracker!")
                return
        
        with open(self.filename, 'r') as file:
            file_list = file.readlines()

        task_index = self.findTask(inputID)

        # updates particular task description 
        task = json.loads(file_list[task_index])
        task["description"] = update 

        # prepare data to write back to file
        file_list[task_index] = json.dumps(task) + '\n'

        with open(self.filename, 'w') as file:
            file.writelines(file_list)

        print(f"Task updated successfully! (ID: {inputID})")

    def deleteTask(self, inputID):
        with open(self.filename, 'r') as file:
            file_list = file.readlines()

        if inputID < 1 or inputID >= len(file):
            print("Task ID not in tracker!")
            print("To view tasks and their IDs, enter 'list'")
            return
        
        task_index = self.findTask(inputID)
        task = json.loads(file_list[task_index])

        

        del task





                    
        
            
            
                 






