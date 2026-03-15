# BLX-UNKNOWN-0
# PROJECT 3 // TO-DO LIST
# Learned: lists, while loop menu, file saving, open(),

def show_tasks (tasks):
    if len(tasks) == 0:
        print("No task yet!\n")
    else:
        print("\n...Your task is ...")
        for i, task in enumerate( tasks, 1):
            print(f"{i}. {task}")
        print()

def save_tasks (tasks):
    with open( "task.txt","w") as f:
        for task in tasks :
            f.write(task + "\n")

def load_tasks ():
    try:
        with open( "task.txt","r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return[]
    
def to_do ():
    print("... TO-DO LIST ... ")
    tasks = load_tasks()

    while True:
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print(f"Added: {task}\n")

        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed}\n")
            except (ValueError, IndexError):
                print("Invalid number!\n")

        elif choice == "4":
            print(" Have a good day , Bye!")
            break

        else:
            print("Invalid choice!\n")

to_do ()

