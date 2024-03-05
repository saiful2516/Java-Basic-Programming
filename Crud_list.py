todos = []
while True:
    user_action = input("Type add, show, update or exit: ")
    user_action =user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todo = todo.strip()
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item.capitalize())

        case 'update' :
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter your todo:")
            todos[number] = new_todo


        case 'exit' :
            break

print("Program finished!")


