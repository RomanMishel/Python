<<<<<<< ours
<<<<<<< ours
tasks_list = {
    "task_name" : "",
    "done" : False,
}

def add_task():
    task_name = input("Enter the task: ")

    task = {
        "task_name": task_name,
        "done": False
    }

    tasks_list.update(task)
    print("Task added!")

def show_tasks_list():
    if len(tasks_list) == 0:
        print("No tasks_list yet.")
        return

    for index, task in enumerate(tasks_list, start=1):
        checkbox = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {checkbox} {task['task_name']}")

def mark_task_done():
    print(tasks_list)
    user_choice = input("What task is done?: ")


def mark_task_done():
    if len(tasks_list) == 0:
        print("No tasks_list to mark as done.")
        return

    show_tasks_list()

    user_choice = input("Which task is done? Enter task number: ")
=======
=======
>>>>>>> theirs
tasks_list = []


def add_task():
    task_name = input("Enter the task: ").strip()

    if task_name == "":
        print("Task name cannot be empty.")
        return

    tasks_list.append({"task_name": task_name, "done": False})
    print("Task added!")


def show_tasks_list():
    if len(tasks_list) == 0:
        print("No tasks yet.")
        return

    for task_number, task in enumerate(tasks_list, start=1):
        checkbox = "[x]" if task["done"] else "[ ]"
        print(f"{task_number}. {checkbox} {task['task_name']}")


def mark_task_as_done():
    if len(tasks_list) == 0:
        print("No tasks to mark as done.")
        return

    show_tasks_list()
    user_choice = input("Which task is done? Enter task number: ").strip()
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs

    if not user_choice.isdigit():
        print("Please enter a number.")
        return

    task_number = int(user_choice)

    if task_number < 1 or task_number > len(tasks_list):
        print("There is no task with this number.")
        return

    task_index = task_number - 1
    tasks_list[task_index]["done"] = True
<<<<<<< ours
<<<<<<< ours

    print("Task marked as done!")


def reset_tasks():
    for task in tasks_list:
        task["done"] = False

    print("All tasks_list were reset.")


while True:
    print()
    print("Welcome to ToDo Tasker!")
=======
=======
>>>>>>> theirs
    print("Task marked as done!")


def reset_tasks_list():
    if len(tasks_list) == 0:
        print("No tasks to reset.")
        return

    for task in tasks_list:
        task["done"] = False

    print("All tasks were reset.")


def show_menu():
    print("\nWelcome to ToDo Tasker!")
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
    print("1. Add task")
    print("2. Show tasks_list")
    print("3. Mark task as Done")
    print("4. Reset tasks_list")
    print("5. Exit")

<<<<<<< ours
<<<<<<< ours
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
=======
=======
>>>>>>> theirs

def main():
    while True:
        show_menu()
        user_input = input("Choose an option: ").strip()

        if user_input == "1":
            add_task()
        elif user_input == "2":
            show_tasks_list()
        elif user_input == "3":
            mark_task_as_done()
        elif user_input == "4":
            reset_tasks_list()
        elif user_input == "5":
            print("Goodbye!")
            break
        else:
            print("Unknown option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
