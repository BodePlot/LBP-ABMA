import PySimpleGUI as sg
from QUERIES import queries
sg.theme("Default")

layout1 = [
    [sg.Text("BSAM 2")],

    
    [sg.Button("Admin Functions")],

]

# Crea la ventana
window = sg.Window("Main Menu", layout1,size=(500,200))


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

    [sg.Text("", size=(10, 1)), sg.Text("Analyst", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Persona 1", "Persona 2", "Persona 3"], size=(15, 1),font=('Arial'), readonly=True),
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

    [sg.Button("OK", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Button("Cancel", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]

    ]



while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Admin Functions":
        # Define el diseño de la segunda ventana

        # Cierra la ventana actual
        window.close()

        window = sg.Window("BISAM", layout2, size=(1500, 700), resizable=True)

window.close()

