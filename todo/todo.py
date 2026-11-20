from datetime import date

class Todo:

    def __init__(self, data_manager):
        self.data_manager = data_manager()
        self.path = "data/tasks/tasks.json"
        self.tasks = self.data_manager.load_data(self.path)

    def add_task(self, title, description=""):
        if not title.strip():
            print("Task title is required!")
            return

        task = {
            "id": max([task["id"] for task in self.tasks], default=0) + 1,
            "title": title.strip(),
            "description": description.strip(),
            "created_at": date.today().isoformat(),
            "completed": False
        }

        self.tasks.append(task)
        self.data_manager.save_data(self.path, self.tasks)

        print("Task added successfully!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return

        for task in self.tasks:
            status = "Done" if task["completed"] else "Not Done"

            print(f'\nID: {task["id"]}')
            print(f'Title: {task["title"]}')
            print(f'Description: {task["description"]}')
            print(f'Date: {task["created_at"]}')
            print(f'Status: {status}')

    def edit_task(self, task_id, new_title, new_description=""):
        if not new_title.strip():
            print("Task title is required!")
            return

        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = new_title.strip()
                task["description"] = new_description.strip()

                self.data_manager.save_data(self.path, self.tasks)
                print("Task updated successfully!")
                return

        print("Task not found!")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.data_manager.save_data(self.path, self.tasks)

                print("Task deleted successfully!")
                return

        print("Task not found!")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True

                self.data_manager.save_data(self.path, self.tasks)

                print("Task completed successfully!")
                return

        print("Task not found!")