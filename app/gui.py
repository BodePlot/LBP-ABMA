import PySimpleGUI as sg


# Define the layout of the window
layout = [
    [sg.Text("Enter your name:")],
    [sg.InputText(key='-NAME-')],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

# Create the window
window = sg.Window('Simple GUI', layout)

# Event loop
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    if event == 'Submit':
        name = values['-NAME-']
        sg.popup(f'Hello, {name}!')
        
# Close the window
window.close()
