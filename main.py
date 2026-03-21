
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
    user_action = input("Type add or show: ")

    match user_action:
        case "add":
            todos.append(user_action)
        case "show":
            print(todos)