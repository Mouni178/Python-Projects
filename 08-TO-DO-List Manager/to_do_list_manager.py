tasks = []
completed_tasks = []
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    completed_tasks.append(False)
    print("Task added successfully!")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("YOUR TASKS")
        for i in range(len(tasks)):
            if completed_tasks[i]:
                print(i + 1, tasks[i], "- Completed")
            else:
                print(i + 1, tasks[i], "- Pending")
def complete_task():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    view_tasks()
    task_number = int(input("Enter task number to complete: "))
    if task_number >= 1 and task_number <= len(tasks):
        completed_tasks[task_number - 1] = True
        print("Task completed!")
    else:
        print("Invalid task number.")
def delete_task():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    view_tasks()
    task_numbr = int(input("Enter task number to delete: "))
    if task_number >= 1 and task_number <= len(tasks):
        tasks.pop(task_number - 1)
        completed_tasks.pop(task_number - 1)
        print("Task deleted!")
    else:
        print("Invalid task number.")
while True:
    print("TO-DO LIST MANAGER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
