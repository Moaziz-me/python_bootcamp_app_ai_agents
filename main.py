
# user_prompt = "Enter todo1: "
#
#
#
# todos = []  # create list ONCE
#
# while True:
#     todo = input(user_prompt)
#     todos.append(todo.capitalize())  # add new item
#     print(todos)


todos = []

while True:
    user_action = input("Type add, show or exit: ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
print("Bye")