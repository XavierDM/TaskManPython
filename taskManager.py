import json

with open("tasks.json", "r") as read_file:
    tasks = json.load(read_file)
""" tasks = ["make bread", "make eclairs"] """
""" complTasks = [] """


while True:
    choice = input("Welcome to the task manager please choose one of following options\n"
    "1. Display tasks\n"
    "2. Add a task\n"
    "3. Delete a task\n"
    "4. Mark a task completed\n"
    "5. Exit the program\n"
    "Please choose a number corresponding to the menu: \n")
    choice = int(choice)
    if choice == 1:
        """ allTasks = tasks + complTasks """
        print(tasks)
    elif choice == 2:
        addTask = input("What task to you want to add?\n")
        tasks.append(addTask)
    elif choice == 3:
        print(tasks)
        delTask = input("Which task do you want to delete?\n")
        tasks.remove(delTask)
        print(delTask, "will be removed\n")
    elif choice == 4:
        print("The current tasks are", tasks,"\n")
        complete = input("Which task did you complete?\n")
        tasks.remove(complete)
        complTask = (complete + " " + "[X]")
        tasks.append(complTask)
        print(tasks)
    elif choice >5:
        print("This is not an option in the menu\n")
    elif choice == 5:
        print("Thank you come again")
        with open("tasks.json", "w") as write_file:
            json.dump(tasks, write_file)
        break
