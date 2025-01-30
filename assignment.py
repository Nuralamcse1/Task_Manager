
import json
import os

class Task(json.JSONEncoder):
    def __init__(self, task_id, description, deadline=None, status='pending'):
        self.id = task_id
        self.description = description
        self.deadline = deadline
        self.status = status
    
    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'deadline':self.deadline,
            'status':self.status
        }
    
    def __str__(self):
                return f"ID: {self.id}, Description: {self.description}, Deadline: {self.deadline}, Status: {self.status}"
    
class TaskManager:
    tasks = []
    def __init__(self, storage_file='tasks.json'):
        self.storage_file = storage_file
        self.tasks = []

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                print(json.loads(str(file.readlines())))
                self.tasks=json.loads(str(file.readlines()))
        return []

    def save_tasks(self):
        with open(self.storage_file, 'w') as file:
            file.write(json.dumps(self.tasks, indent=4))

    def add_task(self, description, deadline=None):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description, deadline)
        self.tasks.append(task.to_dict())
        self.save_tasks()

    def view_tasks(self, status=None):
        for task in self.tasks:
            if status is None or task['status'] == status:
                print(task)

    def update_task(self, task_id, description=None, status=None):
        for task in self.tasks:
            if task['id'] == task_id:
                if description:
                    task['description'] = description
                if status:
                    task['status'] = status
                self.save_tasks()
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()


        
def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Update a task")
        print("6. Delete a task")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (optional): ")
            task_manager.add_task(description, deadline)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.view_tasks(status='pending')
        elif choice == '4':
            task_manager.view_tasks(status='completed')
        elif choice == '5':
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description (leave blank to keep current): ")
            status = input("Enter new status (pending/completed): ")
            task_manager.update_task(task_id, description, status)
        elif choice == '6':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == '7':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()