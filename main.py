todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for index, item in enumerate(todos, start=1):
                item = item.capitalize()
                print(f"""{index}. {item}""")
        case "edit":
            number = int(input("Got it, number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new to do: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number)
        case "exit":
            break
        case whatever:
            print("Hey it does not match any of the cases")
print("Bye")