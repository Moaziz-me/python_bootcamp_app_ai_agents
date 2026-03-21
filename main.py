todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.capitalize()
                print(item)
        case "edit":
            number = int(input("Got it, number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new to do: ")
            todos[number] = new_todo
        case "exit":
            break
        case whatever:
            print("Hey it does not match any of the cases")
print("Bye")