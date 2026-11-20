from data_manager.json_data_manager import DataManager
from todo.todo import Todo

class Cli:

    def __init__(self):
        self.todo = Todo(DataManager)

    def show_menu(self):
        print("\n========== TODO APP ==========")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Complete Task")
        print("6. Exit")

    def add_task(self):
        title = input("Task title: ")
        description = input("Task description (optional): ")

        self.todo.add_task(title, description)

    def show_tasks(self):
        self.todo.show_tasks()
    
    def edit_task(self):
        try:
            task_id = int(input("Task ID: "))
            title = input("New title: ")
            description = input("New description (optional): ")

            self.todo.edit_task(task_id, title, description)

        except ValueError:
            print("Please enter a valid ID!")

    def delete_task(self):
        try:
            task_id = int(input("Task ID: "))
            self.todo.delete_task(task_id)

        except ValueError:
            print("Please enter a valid ID!")

    def complete_task(self):
        try:
            task_id = int(input("Task ID: "))
            self.todo.complete_task(task_id)

        except ValueError:
            print("Please enter a valid ID!")

    def run(self):
        while True:
            self.show_menu()

            choice = input("Select an option: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.show_tasks()

            elif choice == "3":
                self.edit_task()

            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                self.complete_task()

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid option!")