task = []

def add():
    add_task = input("Enter the added task :")
    task.append(add_task)

def view():
    if not task:
        return ("task is not view")
    else:
        i = 1
        for t in task:
            print(i, t)
            i += 1

def remove():
    index = int(input("Enter task need to remove :"))
    task.pop(index-1)

while True:
    print("\n1. View\n2. Add\n3. Remove\n4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        remove()
    elif choice == "4":
        break
    else:
        print("Invalid choice")











