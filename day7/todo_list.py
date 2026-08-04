while True:
    print("\n=======To-Do List=======")
    print("1. Add Task")
    print("2. view Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "4":
        print("Thank You For Using To-Do List!")
        break

    elif choice == "1":
        task = input("Enter your task:")
        with open("day7/tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task Added successfully!")
    
    elif choice == "2":
         try:
            with open("day7/tasks.txt", "r") as file:
                tasks = file.readlines()

            if tasks == []:
                    print("No Tasks Found!")

            else:
                print("\n=======Your Tasks=======")
                number = 1
                for task in tasks:
                     print(f"{number}. {task.strip()}")
                     number += 1
         except FileNotFoundError:
            print("No Tasks Found!")

    elif choice == "3":
        try:
            with open("day7/tasks.txt", "r") as file:
                task_list = file.readlines()

            task_number = int(input("Enter the task number to delete: "))

            if 1 <= task_number <= len(task_list):
               del task_list[task_number - 1]

               with open("day7/tasks.txt", "w") as file:
                 file.writelines(task_list)

               print("Task deleted successfully!")
            else:
                print("Invalid task number!")

        except FileNotFoundError:
            print("no tasks found!")        

        except ValueError:
            print("Please enter valid number!")      
