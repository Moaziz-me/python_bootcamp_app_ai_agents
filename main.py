
user_prompt = "Enter todo1: "



todos = []  # create list ONCE

while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize())  # add new item
    print(todos)