import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="input_box", key='Todo')
add_button = sg.Button("Add")

Window = sg.Window("My To-do App",
                   layout=[[label], [input_box, add_button]],
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
        case sg.WIN_CLOSED:
            break
Window.close()
