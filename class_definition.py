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
                fileSize = os.path.getsize(file)

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
                print(f"Task added successfully (ID: {lastId + 1})")
        except Exception as e:
            print(f"Failed to append to file, {e}")
    
    def updateTask(self, id):
        with open(self.filename, 'a') as file:
            if not os.path.exists(file):
                print("No task available in tracker!")
                return
            file_list = file.readlines()
            l = 0
            r = len(file_list)
            count = r // 2
            while l <= r:
                if file_list[l] > file_list[count]:





