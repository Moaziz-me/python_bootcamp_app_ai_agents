import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="input_box", key='Todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))

edit_button = sg.Button("Edit")

Window = sg.Window("My To-do App",
                   layout=[[label],
                           [input_box, add_button, edit_button],
                           [list_box]
                           ],
                   font=('Helvetica', 20),)

while True:
    event, values = Window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['Todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            Window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['Todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            Window["todos"].update(values=todos)

        case 'Todo':
            Window["Todo"].update(values=values['todos'])

        case sg.WIN_CLOSED:
            break


Window.close()
