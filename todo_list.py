tasks_list = []

def add_task():
    task_name = input("Enter the task: ")

    task = {
        "task_name": task_name,
        "done": False
    }

    tasks_list.append(task)
    print("Task added!")

def show_tasks_list():
    if len(tasks_list) == 0:
        print("No tasks_list yet.")
        return

    for index, task in enumerate(tasks_list, start=1):
        checkbox = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {checkbox} {task['task_name']}")

def mark_task_done():
    if len(tasks_list) == 0:
        print("No tasks_list to mark as done.")
        return

    show_tasks_list()

    user_choice = input("Which task is done? Enter task number: ")

    if not user_choice.isdigit():
        print("Please enter a number.")
        return

    task_number = int(user_choice)

    if task_number < 1 or task_number > len(tasks_list):
        print("There is no task with this number.")
        return

    task_index = task_number - 1
    tasks_list[task_index]["done"] = True

    print("Task marked as done!")


def reset_tasks():
    tasks_list.clear()

    print("Tasks list was cleared.")


while True:
    print()
    print("Welcome to ToDo Tasker!")
    print("1. Add task")
    print("2. Show tasks_list")
    print("3. Mark task as Done")
    print("4. Reset tasks_list")
    print("5. Exit")

    user_input = input("Choose an option: ")

    if user_input == "1":
        add_task()

    elif user_input == "2":
        show_tasks_list()

    elif user_input == "3":
        mark_task_done()

    elif user_input == "4":
        reset_tasks()

    elif user_input == "5":
        print("Goodbye!")
        break

    else:
        print("Unknown option. Please choose from 1 to 5.")
