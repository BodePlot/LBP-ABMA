import PySimpleGUI as sg
from QUERIES import queries

# Definimos los temas para la GUI
sg.theme("Default")

layout1 = [
    [sg.Text("", size=(60, 1)), sg.Text("Reporting month:", text_color="#024A86",font=("Arial", 13, "bold"))],
    [sg.Text("BSAM 2",font=("Verdana", 60),pad=(93,1), text_color="#024A86")],
    [sg.Text("", size=(13, 1),pad=(1,6))],
    [sg.Button("All Acounts",size=(18,2),pad=(100,10),font=("Arial", 15, "bold"),button_color=("#024A86", "#ccffff"))],
    [sg.Button("Admin Functions",size=(18,2),pad=(100,10),font=("Arial", 15, "bold"),button_color=("#024A86", "#ccffff"))],
    [sg.Button("Reports Menu",size=(18,2),pad=(100,10),font=("Arial", 15, "bold"),button_color=("#024A86", "#ccffff"))],
    [sg.Text("", size=(13, 1),pad=(1,10))],
    [sg.Button("Exit", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]
]

# Crea la ventana
window = sg.Window("Main Menu", layout1,size=(800,500))

menu_def = ['Reconciling item',
    [
        'List Component 1',
            [['Bin A               ::algo', 'Bin B::algos','Bin A::13', 'Bin B::algod']],

        'Rack 2',
            [['Bin A          ::21', 'Bin B::22', 'Bin B::23', 'Bin B::24']],

        'Rack 3',
            [['Bin A       ::21']],

    ]
]

# Datos para llenar la tabla
data = queries(state='juan')

# Encabezados de la tabla
headings = ['Account', 'Posted','DT', 'CoCd', 'Allocation', 'Textline','TaxType', 'Amount', 'State', 'DueDate', 'Age', '# Trans', 'Audit', 'Completed' ]

# Creamos el diseño de la ventana
layout2 = [
    [sg.Button("Go back", size=(8,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("Analyst", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Persona 1", "Persona 2", "Persona 3"], size=(15, 1),font=('Arial'), readonly=True),
     sg.Text("State", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(10, 1), background_color='lightgray', disabled=True),
     sg.Text("#Items", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(len(data), key="-ITEMS-", size=(7, 1), background_color='lightgray', disabled=True),
     sg.Text("Status", text_color="#024A86",font=('Arial', 12, "bold")), sg.Input(key="-STATUS-", size=(18, 1), background_color='lightgray', disabled=True),
     sg.Text("Type", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(data, size=(12, 1),font=('Arial'), readonly=True),
     sg.Text("Age", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL AGED", "ALL AGEDss"], size=(12, 1),font=('Arial'), readonly=True),
     sg.Text("Audit Hold", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL ITEMS"], pad=(10, 25), size=(15, 1),font=('Arial'), readonly=True)]
     ,

    [sg.Text("", size=(10, 1)), sg.Text("Reporting month:", text_color="#024A86"), sg.Text("", size=(117, 1)), sg.Text(" Completed", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["All"], size=(8, 1),font=('Arial'), readonly=True)],

    [sg.Text("", pad=(1, 1))],

    [sg.Text("", size=(1, 1)),
    sg.Table(
        values=data,
        headings=headings,
        max_col_width=200,
        def_col_width=10,
        auto_size_columns=False,
        num_rows=15,
        key="-TABLE-", 
        background_color='#C0C0C0',
        header_text_color='black'
    ), sg.Text("", size=(1, 1)), sg.Button("SAP Report", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))],


    [sg.Text("Category                       ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Optiona", "Options", "Optiodn"], size=(20, 1), readonly=True), sg.Text("", size=(13, 1)), sg.Text("Original Month",text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],
     
    [sg.Text("Statute of Limitation  ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")),sg.Input(key="-STATE-", size=(20, 10), background_color='lightgray'), sg.Text("", size=(15, 1)), sg.Text("End Month       ", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],

    [sg.Text("Collaboration Tool ID", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-COLABTOOL-", size=(20, 10), background_color='lightgray')],

    [sg.Text("", size=(57, 1)), sg.Button("Update", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("", size=(10, 1)), sg.ButtonMenu('Location', menu_def=menu_def, key='Button_Menu', button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"), size=(20,1))],

    [sg.Text("", pad=(10, 10))],

    [sg.Button("OK", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Button("Exit", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]

    ]




# Creamos la ventana con un tamaño grande (ancho, alto)
# window = sg.Window("BISAM", layout1, size=(1500, 700), resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "Admin Functions":
        window.close()
        layout2 = [
            [sg.Button("Go back", size=(8,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("Analyst", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Persona 1", "Persona 2", "Persona 3"], size=(15, 1),font=('Arial'), readonly=True),
            sg.Text("State", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(10, 1), background_color='lightgray', disabled=True),
            sg.Text("#Items", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(len(data), key="-ITEMS-", size=(7, 1), background_color='lightgray', disabled=True),
            sg.Text("Status", text_color="#024A86",font=('Arial', 12, "bold")), sg.Input(key="-STATUS-", size=(18, 1), background_color='lightgray', disabled=True),
            sg.Text("Type", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(data, size=(12, 1),font=('Arial'), readonly=True),
            sg.Text("Age", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL AGED", "ALL AGEDss"], size=(12, 1),font=('Arial'), readonly=True),
            sg.Text("Audit Hold", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL ITEMS"], pad=(10, 25), size=(15, 1),font=('Arial'), readonly=True)]
            ,

            [sg.Text("", size=(10, 1)), sg.Text("Reporting month:", text_color="#024A86"), sg.Text("", size=(117, 1)), sg.Text(" Completed", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["All"], size=(8, 1),font=('Arial'), readonly=True)],

            [sg.Text("", pad=(1, 1))],

            [sg.Text("", size=(1, 1)),
            sg.Table(
                values=data,
                headings=headings,
                max_col_width=200,
                def_col_width=10,
                auto_size_columns=False,
                num_rows=15,
                key="-TABLE-", 
                background_color='#C0C0C0',
                header_text_color='black'
            ), sg.Text("", size=(1, 1)), sg.Button("SAP Report", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))],


            [sg.Text("Category                       ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Optiona", "Options", "Optiodn"], size=(20, 1), readonly=True), sg.Text("", size=(13, 1)), sg.Text("Original Month",text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],
            
            [sg.Text("Statute of Limitation  ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")),sg.Input(key="-STATE-", size=(20, 10), background_color='lightgray'), sg.Text("", size=(15, 1)), sg.Text("End Month       ", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],

            [sg.Text("Collaboration Tool ID", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-COLABTOOL-", size=(20, 10), background_color='lightgray')],

            [sg.Text("", size=(57, 1)), sg.Button("Update", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("", size=(10, 1)), sg.ButtonMenu('Location', menu_def=menu_def, key='Button_Menu', button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"), size=(20,1))],

            [sg.Text("", pad=(10, 10))],

            [sg.Button("OK", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Button("Exit", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]

            ]

        window = sg.Window("BISAM", layout2, size=(1500, 700), resizable=True)

    if event == "Go back":

        window.close()
        layout1 = [
        [sg.Text("BSAM 2")],

        
        [sg.Button("All Acounts")],
        [sg.Button("Admin Functions")],
        [sg.Button("Reports Menu")]
    ]

        window = sg.Window("Main Menu", layout1,size=(500,200),resizable=True)

    if event == "OK":

        state=str(values['-STATE-'])
        items=str(values['-ITEMS-'])
        status=str(values['-STATUS-'])

        data=queries(state)
        
        window["-TABLE-"].update(values=data)
    
    if event == "Update":
        data=[]
        window["-TABLE-"].update(values=data)
        window["-ITEMS-"].update(len(data))
    
    if event == "SAP Report":
        name=52222
        age=22
        gender=33
        cronico=11
        # Añade una nueva fila de datos a la lista 'data'
        data.append([name, age, gender, cronico])
        # Actualiza el contenido de la tabla
        window["-TABLE-"].update(values=data)
        window["-ITEMS-"].update(len(data))

window.close()