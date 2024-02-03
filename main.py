# TODO Application
# todos = []
while True:
    user_prompt = input("Type Add , Show , Edit , Complete or Exit: ").strip()
    match user_prompt:
        case "add":
            todo = input("Enter item to add in todo list:") + "\n"
            # item= item.strip()
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            print("Todo list contains:")
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                # item = item.strip().title()
                # print(type(item))
                row = f" {index + 1}. {item.strip().title()}"
                print(row)
        case "edit":
            item_number = int(input('Enter item number:'))
            item_number = item_number - 1
            new_item = input('Enter new item:').strip()
            todos[item_number] = new_item
            # todos.append()
        case 'complete':
            item_number = int(input('Enter item number:'))
            item_number = item_number - 1
            todos.pop(item_number)
        case "exit":
            print("Bye!")
            break
        case _:
            print("Invalid input")
