# TODO Application
# todos = []
while True:
    user_prompt = input("Choose -: Add , Show , Edit , Complete or Exit: ").strip()
    if 'add' in user_prompt:
        todo = user_prompt[4:]
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)
        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

        print('list updated')

    elif 'show' in user_prompt:
        print("Todo list contains:")

        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            # item = item.strip().title()
            # print(type(item))
            row = f" {index + 1}. {item.strip().title()}"
            print(row)

    elif 'edit' in user_prompt:
        #item_number = int(input('Enter item number:'))
        item_number = int(user_prompt[5:]) - 1

        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()
        print('Existing todo items list :- ', todos)
        print('\n')

        new_item = input('Enter new item:').strip()
        todos[item_number]= new_item + '\n'
        print('\n')

        print('New todo items list :- ', todos)
        print('\n')

        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

        greeting = f'New todo item replaced with name = {new_item} in position = {item_number+1} in the list'
        print(greeting)
        print('list updated')

    elif 'complete' in user_prompt:

        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()
        print('Existing todo items list :- ', todos)
        print('\n')

        #item_number = int(input('Enter item number to remove :'))
        item_number = int(user_prompt[9:]) - 1
        element = todos.pop(item_number)

        print(element)

        print('New todo items list :- ', todos)
        print('\n')

        greeting = f'item removed with name = {element} from position = {item_number+1} from the list.'
        print(greeting)

        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

        print('list updated')

    elif 'exit' in user_prompt:
        break
    else:
        print('you have chosen invalid choice.')
