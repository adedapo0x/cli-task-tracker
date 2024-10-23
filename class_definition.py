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
            with open(self.filename, 'rb') as file:
                file.seek(0, os.SEEK_END)
                fileSize = file.tell()
                
                if fileSize == 0:
                    return 0
                
                # Move the cursor to the beginning of the last line
                file.seek(-1, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
                    if file.tell() == 0:
                        break
                
                last_line = file.readline().decode('utf-8').strip()
                print(last_line)
                last_object = json.loads(last_line)
                return last_object.get("id", 0)
        except (IOError, json.JSONDecodeError) as err:
            print(f"Failed to parse: {err}")
            return 0
        #     with open(self.filename, 'r', encoding='utf-8') as file:
        #         fileSize = os.path.getsize(self.filename)

        #         if fileSize == 0:
        #             return 0
        #         for line in file:
        #             pass
        #         last_line = line.strip()
        #         last_object = json.loads(last_line)
        #         return last_object.get("id", 0)
        # except Exception as err:
        #         print(f"Failed to parse, {err}")

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


    def updateTask(self, inputID, update):
        if not os.path.exists(self.filename):
                print("No task available in tracker!")
                return
        
        with open(self.filename, 'r') as file:
            file_list = file.readlines()

        task_json = file_list[int(inputID) - 1]

        # updates particular task description 
        task = json.loads(task_json)
        task["description"] = update 

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
        
        data = [obj for obj in data if int(obj["id"]) != inputID]

        for i, obj in enumerate(data,start=1):
            obj["id"] = i
        
        with open(self.filename, 'w') as file:
            for obj in data:
                json_str = json.dumps(obj)
                file.write(json_str + '\n')
            
            file.write('\n')

        print("Delete operation successful")






