import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="input_box")
add_button = sg.Button("Add")

Window = sg.Window("My To-do App", layout=[[label], [input_box, add_button]])
Window.read()
Window.close()
