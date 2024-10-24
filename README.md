# cli-task-tracker

cli-task-tracker is a command line interface application where one can track and manage tasks. It tracks what you need to do, what you have done, and what you are currently working on.

The application runs from the command line, accept user actions and inputs, and store the tasks in a JSONL file. This project helped me practice my programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Features
- Add new tasks and stores it in a JSONL file
- Update the description of an existing task
- List tasks by their status: `todo`, `in-progress`, or `done`
- List all tasks present in the tracker
- Mark tasks as in-progress or done, or re-mark as todo after changing to in-progress or done if need be
- Delete task by their unique ID

**Prerequisite** - Python installed on your computer

### Clone the Repository
```bash
git clone https://github.com/adedapo0x/cli-task-tracker

# Navigate to project directory
cd cli-task-tracker
```
### Usage
- **To run application**
``` bash
python tracker.py
```
- **To add a task**
``` bash
add Doing the laundry
```
- **Update task description**
``` bash
update 1 Making dinner
```
- **Listing tasks by their status of completion**
  
``` bash
# To list tasks that are marked as todo
list todo

# To list tasks marked as in-progress
list in-progress

# To list tasks marked as done
list done
```
- **To list all tasks present in tracker**
``` bash
list
```
- **Mark tasks as in-progress, done, or remark as todo**
  
``` bash
# Mark task with ID 1 as `in-progress`
mark-in-progress 1

# Mark task with ID 1 as `done`
mark-done 1

# Re-mark task with ID 1 as `todo` after marking it as something else
mark-to-do 1
```
**Note**: When tasks are initially added to the tracker, they are assigned a default status of `todo` 

- **Delete a task**
``` bash
delete 1
```

### Sample JSONL file structure
```JSONL
{"id": 1, "description": "Doing the laundry", "status": "todo", "createdAt": "2024-10-24 14:07:32", "updatedAt": null}
{"id": 2, "description": "Do my grocery shopping", "status": "done", "createdAt": "2024-10-24 14:07:32", "updatedAt": "2024-10-24 14:08:54"}
```
