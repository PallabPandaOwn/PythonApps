# #user prompt
todos = []
while True:
    user_prompt = input("Add or Show or Exit: ")
    user_prompt=user_prompt.strip()
    match user_prompt:
        case    "add":
            item = input("Enter item to add in todo list:")
            item= item.strip()
            todos.append(item)
        case    "show":
            print("Todo list contains:")
            for item in todos:
                print(item)
        case    "exit":
            print("Bye!")
            break




# prompt = "Enter a ToDo -:"
#
# todos = []
#
# while True:
#     user_prompt1 = input(prompt)
#     todos.append(user_prompt1)
#     print(todos)
# name = "pallab"
# while True:
#
#     print(name.capitalize())
import upper

# while True:
#     name = input("Enter name -")
#     up =name.upper()
#     print(up)

