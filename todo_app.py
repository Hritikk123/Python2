import os

def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

def view_todo_list(todo_list):
    print("\n===== To-Do List =====")
    if not todo_list:
        print("No tasks found.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, new_task):
    todo_list.append(new_task)
    print(f"\nTask '{new_task}' added successfully!")

def mark_task_as_done(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        done_task = todo_list.pop(task_index - 1)
        print(f"\nTask '{done_task}' marked as done!")
    else:
        print("\nInvalid task index.")

def main():
    todo_list = []

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(todo_list, new_task)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as done: "))
            mark_task_as_done(todo_list, task_index)
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()