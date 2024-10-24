from class_definition import FileManager

print("Welcome to Task-Tracker!!")
print("Use commands 'add', 'remove' and co to use the application, press 'help' to get more information")

finished = False

record = FileManager('record.jsonl')

while not finished:
    input_command = input()
    splitted_input = input_command.split() 
    
    if splitted_input[0].lower() == "add":
        task = ' '.join(splitted_input[1:])
        if len(task) < 3:
            print("Please include task, description must have more than two characters")
        else:
            record.addToFile(task)

    elif splitted_input[0].lower() == "update":
        task = " ".join(splitted_input[2:])
        if len(task) >= 3 and splitted_input[1].isdigit():
            record.updateTask(splitted_input[1], task)
        else:
            print("Please include task, description length must be more than two")
            print("ID must be a digit corresponding to a task ID")
            print("To view tasks and their IDs, enter 'list'")

    elif splitted_input[0].lower() == "delete":
        if not splitted_input[1].isdigit():
            print("Enter valid task ID! Enter 'list' to see list of tasks")
        else:
            record.deleteTask(splitted_input[1])
        
    elif splitted_input[0].lower() == "mark-in-progress":
        if not splitted_input[1].isdigit():
            print("Enter valid task ID! Enter 'list' to see list of tasks")
        else:
            record.updateProgress(splitted_input[1], "inProgress")

    elif splitted_input[0].lower() == "mark-to-do":
        if not splitted_input[1].isdigit():
            print("Enter valid task ID! Enter 'list' to see list of tasks")
        else:
            record.updateProgress(splitted_input[1], "toDo")
    
    elif splitted_input[0].lower() == "mark-done":
        if not splitted_input[1].isdigit():
            print("Enter valid task ID! Enter 'list' to see list of tasks")
        else:
            record.updateProgress(splitted_input[1], "done")

    elif splitted_input[0].lower() == "list":
        record.listAllTask()

    elif splitted_input[0].lower() == "end":
        finished = True

    else:
        print("L")
    
    








