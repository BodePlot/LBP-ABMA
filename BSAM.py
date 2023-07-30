import PySimpleGUI as sg
from QUERIES import queries
from datetime import datetime, timedelta

# Definimos los temas para la GUI
sg.theme("Default")

def get_date():
    current_date = datetime.now()
    first_day_current_month = current_date.replace(day=1)
    last_day_past_month = first_day_current_month - timedelta(days=1)

    past_month = last_day_past_month.strftime("%Y/%m")
    return past_month

past_month=get_date()

def layout_main():
    layout_main = [
        [sg.Text("", size=(60, 1)), sg.Text(f"Reporting month: {past_month}", text_color="#024A86",font=("Arial", 13, "bold"))],
        [sg.Text("BSAM 2",font=("Verdana", 60),pad=(93,1), text_color="#024A86")],
        [sg.Text("", size=(13, 1),pad=(1,6))],
        [sg.Button("All Acounts",size=(18,2),pad=(100,10),font=("Arial", 15, "bold"),button_color=("#024A86", "#ccffff"))],
        [sg.Button("Admin Functions",size=(18,2),pad=(100,10),font=("Arial", 15, "bold"),button_color=("#024A86", "#ccffff"))],
        [sg.Button("Reports Menu",size=(18,2),pad=(100,10),font=("Arial", 15, "bold"),button_color=("#024A86", "#ccffff"))],
        [sg.Text("", size=(13, 1),pad=(1,10))],
        [sg.Button("Exit", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]
    ]
    return layout_main


window = sg.Window("Main Menu", layout_main(),size=(800,500))
data= queries('juan','azra')

def layout_admin():
    # menu_def = ['Reconciling item',
    #     [
    #         'List Component 1',
    #             [['Bin A', 'Bin B::algos','Bin A::13', 'Bin B::algod']],

    #         'Rack 2',
    #             [['Bin A          ::21', 'Bin B::22', 'Bin B::23', 'Bin B::24']],

    #         'Rack 3',
    #             [['Bin A       ::21']],
    #     ]
    # ]

    # menu_def =  [
    #             ['File', ['Open', 'Save','Exit']],
    #             ['Edit', ['Paste', ['Special','Normal'], 'Undo']],
    #             ['Help', 'About']
    #             ]

    menu_defa = [['File', ['New', 'Open', 'Save', 'Exit', ]], ['Edit', ['Cut', 'Copy', 'Paste', 'Undo'], ],  ['Help', 'About...'] ]

    

    headings = ['Account', 'Posted','DT', 'CoCd', 'Allocation', 'Textline','TaxType', 'Amount', 'State', 'DueDate', 'Age', '# Trans', 'Audit', 'Completed' ]

    layout_admin = [
        [sg.Button("Go back", size=(8,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("Analyst", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Persona 1", "Persona 2", "Persona 3"], size=(15, 1),font=('Arial'), readonly=True),
        sg.Text("State", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(10, 1), background_color='lightgray', disabled=True),
        sg.Text("#Items", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(len(data), key="-ITEMS-", size=(7, 1), background_color='lightgray', disabled=True),
        sg.Text("Status", text_color="#024A86",font=('Arial', 12, "bold")), sg.Input(key="-STATUS-", size=(18, 1), background_color='lightgray', disabled=True),
        sg.Text("Type", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(data, size=(12, 1),font=('Arial'), readonly=True),
        sg.Text("Age", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL AGED", "ALL AGEDss"], size=(12, 1),font=('Arial'), readonly=True),
        sg.Text("Audit Hold", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL ITEMS"], pad=(10, 25), size=(15, 1),font=('Arial'), readonly=True)],
        [sg.Text("", size=(10, 1)), sg.Text(f"Reporting month: {past_month}", text_color="#024A86", font=("Arial", 12, "bold")), sg.Text("", size=(106, 1)), sg.Text("Completed", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["All"], size=(8, 1),font=('Arial'), readonly=True)],
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
        header_text_color='black'), 
        
        sg.Text("", size=(1, 1)), sg.Button("SAP Report", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))],
        [sg.Text("Category                       ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Optiona", "Options", "Optiodn"], size=(20, 1), readonly=True), sg.Text("", size=(13, 1)), sg.Text("Original Month",text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],
        [sg.Text("Statute of Limitation  ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")),sg.Input(key="-STATE-", size=(20, 10), background_color='lightgray'), sg.Text("", size=(15, 1)), sg.Text("End Month       ", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],
        [sg.Text("Collaboration Tool ID", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-COLABTOOL-", size=(20, 10), background_color='lightgray')],
        [sg.Text("", size=(57, 1)), sg.Button("Update", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("", size=(10, 1)), sg.ButtonMenu('Location', menu_defa,  key='-Button_Menu-', button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"), size=(20,1))],
        [sg.Text("", pad=(10, 10))],
        [sg.Button("OK", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Button("Exit", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]
        ]
    
    return layout_admin

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        
        break

    if event == "Admin Functions":

        window.close()
        window = sg.Window("BISAM", layout_admin(), size=(1500, 700), resizable=True)

    if event == "Go back":

        window.close()
        window = sg.Window("Main Menu", layout_main(),size=(800,500),resizable=True)

    if event == "OK":

        state=str(values['-STATE-'])
        items=str(values['-ITEMS-'])
        status=str(values['-STATUS-'])
    
    if event == "Update":

        data=[]
        window["-TABLE-"].update(values=data)
        window["-ITEMS-"].update(len(data))
    
    if event == "SAP Report":

        name="Persona 1"
        age=22
        gender=33
        cronico=11
        data.append([name, age, gender, cronico])
        window["-TABLE-"].update(values=data)
        window["-ITEMS-"].update(len(data))

    if event=='-Button_Menu-':
        selected_menu = values['-Button_Menu-']

        if selected_menu=='Paste':    
            
            print('jajaja')

window.close()