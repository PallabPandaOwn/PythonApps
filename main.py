# TODO Application
todos = []
while True:
    user_prompt = input("Type Add , Show , Edit or Exit: ")
    user_prompt = user_prompt.strip()
    match user_prompt:
        case "add":
            item = input("Enter item to add in todo list:").strip()
            # item= item.strip()
            todos.append(item)
        case "show":
            print("Todo list contains:")
            for item in todos:
                item = item.strip().title()
                print(item)
        case "edit":
            item_number = int(input('Enter item number:'))
            item_number = item_number - 1
            new_item = input('Enter new item:').strip()
            todos[item_number] = new_item
            # todos.append()
        case "exit":
            print("Bye!")
            break
        case _:
            print("Invalid input")
