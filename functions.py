def get_todos(filepath = "todos.txt"):
    """
    Read a text file and return a list of the todos
    """
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, file_path = "todos.txt"):
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_arg)
