task_list = {
    "task_name" : "",
    "done" : False
}

print(f"Welcome to ToDo Tasker!\n 1.Add task\n 2.Show tasks\n 3.Mark task as Done\n 4.Reset task")

user_input = str(input("Choose an option: "))
if user_input == "1":
    def add_task():
        user_option_1 = str(input("Enter the task: "))
        task_list.update({"task_name" : user_option_1, "done": False})

elif user_input == "2":
    def show_tasks():
        print(task_list)

elif user_input == "3":
    def mark_task_done():
        