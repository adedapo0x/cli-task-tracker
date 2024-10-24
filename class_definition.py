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
                "status": "todo",
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
        try:
            with open(self.filename, 'r') as file:
                file_list = file.readlines()
        except Exception as e:
            print(f"Problem encountered while reading tracker data, error: {e}")

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

        try:
            with open(self.filename, 'w') as file:
                file.writelines(file_list)
        except Exception as e:
            print("Problem encountered while updating tracker, err: {e}")
        print(f"Task updated successfully! (ID: {inputID})")

    def deleteTask(self, inputID):
        if not os.path.exists(self.filename):
                print("No task available in tracker!")
                return
        data = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    data.append(json.loads(line.strip()))
        except Exception as e:
            print(f"Problem getting tracker data, error: {e}")

        if int(inputID) < 1 or int(inputID) > len(data):
            print("Task ID not in tracker!")
            print("To view tasks and their IDs, enter 'list'")
            return
        
        data = [obj for obj in data if obj["id"] != int(inputID)]

        for i, obj in enumerate(data,start=1):
            obj["id"] = i
        
        try:
            with open(self.filename, 'w') as file:
                for obj in data:
                    json_str = json.dumps(obj)
                    file.write(json_str + '\n')
        except Exception as e:
            print(f"Problem encountered while updating tracker, error: {e}")
        print("Delete operation successful")

    def updateProgress(self, inputID, progress):
        if not os.path.exists(self.filename):
            print("No task available in tracker!")
            return
        
        try:
            with open(self.filename, 'r') as file:
                file_list = file.readlines()
        except Exception as e:
            print(f"Problem reading tracker, error: {e}")

        if int(inputID) < 1 or int(inputID) > len(file_list):
            print("Task ID not in tracker!")
            print("To view tasks and their IDs, enter 'list'")
            return
        
        task_json = file_list[int(inputID) - 1]
        task = json.loads(task_json)

        if task["status"] == progress:
            print(f"Task status is already in: {progress}!")
            return 

        task["status"] = progress

        file_list[int(inputID) - 1] = json.dumps(task) + "\n"
        try:
            with open(self.filename, 'w') as file:
                file.writelines(file_list)
        except Exception as e:
            print(f"Problem updating tracker, error: {e}")

        print(f"Task {inputID} status is now: {progress}!")

    def listAllTask(self):
        if not os.path.exists(self.filename):
            print("No task available in tracker!")
            return
        data = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data.append(json.loads(line.strip()))
        except Exception as e:
            print(f"Problem getting tracker data, error: {e}")

        print("Task ID -- Task -- Status -- Created At -- Updated At")

        for line in data:
            print(f'{line["id"]} - {line["description"]} - {line["status"]} - {line["createdAt"]} - {line["updatedAt"]}')
    

    def listProgress(self, progress):
        if not os.path.exists(self.filename):
            print("No task available in tracker!")
            return
        data = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data.append(json.loads(line.strip()))
        except Exception as e:
            print(f"Problem getting tracker data, error: {e}")

        print("Task ID -- Task -- Status -- Created At -- Updated At")

        for line in data:
            if line["status"] == progress:
                print(f'{line["id"]} - {line["description"]} - {line["status"]} - {line["createdAt"]} - {line["updatedAt"]}')








