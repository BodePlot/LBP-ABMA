import PySimpleGUI as sg
from QUERIES import queries, querie_all
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

#Todo lo que sea condiciones iniciales
data= queries('juan','azra')  #tabla inicial


# data_dropdown= queries('juan','azra')[0]
# flat_data_dropdown = [item for sublist in data_dropdown for item in sublist]
# data_dropdown_type= [str(r) for r in flat_data_dropdown]

data_state=querie_all('azra')

data_status=querie_all('espsar')


def layout_admin():
    
    headings = ['Account', 'Posted','DT', 'CoCd', 'Allocation', 'Textline','TaxType', 'Amount', 'State', 'DueDate', 'Age', '# Trans', 'Audit', 'Completed' ]
    menu_def =  [
                [], 
                ['List Component',      [['Filed Claim','Unfiled Claim', 'Refund Collected', 'Deposit']] , 
                 'Timing Component',    [['Next Return ','Amend', 'Other Jur Return', 'TPP']],
                 'Required Adjustment', [['Taxability Issue']] 
                 ]]

    layout_admin = [
        [sg.Button("Go back", size=(8,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("Analyst", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Persona 1", "Persona 2", "Persona 3"], size=(15, 1),font=('Arial'), readonly=True),
        sg.Text("State", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(data_state, key="-STATE-", size=(10, 1), background_color='lightgray', disabled=True),
        sg.Text("#Items", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(len(data), key="-ITEMS-", size=(7, 1), background_color='lightgray', disabled=True),
        sg.Text("Status", text_color="#024A86",font=('Arial', 12, "bold")), sg.Input(data_status, key="-STATUS-", size=(18, 1), background_color='lightgray', disabled=True),
        sg.Text("Type", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown("jaja", size=(12, 1),font=('Arial'), readonly=True),
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
        [sg.Text("", size=(57, 1)), sg.Button("Update", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("", size=(10, 1)), sg.ButtonMenu('Reconciling Item', menu_def,  key='-Button_Menu-', button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"), size=(20,1))],
        [sg.Text("", pad=(10, 10))],
        # [sg.Image("Sin título.png", size=(250,250))],
        [sg.Button("OK", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Button("Exit", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]
        ]
    
    return layout_admin


def layout_tres():
    
    headings = ['Account', 'Posted','DT', 'CoCd', 'Allocation', 'Textline','TaxType', 'Amount', 'State', 'DueDate', 'Age', '# Trans', 'Audit', 'Completed' ]
    menu_def =  [
                [], 
                ['List Component',      [['Filed Claim','Refund Collected', 'Deposit']] , 
                 'Timing Component',    [['Next Return ','Amend', 'Other Jur Return', 'TPP']],
                 'Required Adjustment', [['Taxability Issue']] 
                 ]]

    # layout_tres = [
    #     [sg.Button("Go back", size=(8,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("Analyst", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Persona 1", "Persona 2", "Persona 3"], size=(15, 1),font=('Arial'), readonly=True),
    #     sg.Text("State", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(data_state, key="-STATE-", size=(10, 1), background_color='lightgray', disabled=True),
    #     sg.Text("#Items", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(len(data), key="-ITEMS-", size=(7, 1), background_color='lightgray', disabled=True),
    #     sg.Text("Status", text_color="#024A86",font=('Arial', 12, "bold")), sg.Input(data_status, key="-STATUS-", size=(18, 1), background_color='lightgray', disabled=True),
    #     sg.Text("Type", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(data_dropdown_type, size=(12, 1),font=('Arial'), readonly=True),
    #     sg.Text("Age", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL AGED", "ALL AGEDss"], size=(12, 1),font=('Arial'), readonly=True),
    #     sg.Text("Audit Hold", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["ALL ITEMS"], pad=(10, 25), size=(15, 1),font=('Arial'), readonly=True)],
    #     [sg.Text("", size=(10, 1)), sg.Text(f"Reporting month: {past_month}", text_color="#024A86", font=("Arial", 12, "bold")), sg.Text("", size=(106, 1)), sg.Text("Completed", text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["All"], size=(8, 1),font=('Arial'), readonly=True)],
    #     [sg.Text("", pad=(1, 1))],
    #     [sg.Text("", size=(1, 1)),
         
    #     sg.Table(
    #     values=data,
    #     headings=headings,
    #     max_col_width=200,
    #     def_col_width=10,
    #     auto_size_columns=False,
    #     num_rows=15,
    #     key="-TABLE-", 
    #     background_color='#C0C0C0',
    #     header_text_color='black'), 
        
    #     sg.Text("", size=(1, 1)), sg.Button("SAP Report", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))],
    #     [sg.Text("Category                       ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.DropDown(["Optiona", "Options", "Optiodn"], size=(20, 1), readonly=True), sg.Text("", size=(13, 1)), sg.Text("Original Month",text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],
    #     [sg.Text("Statute of Limitation  ", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")),sg.Input(key="-STATE-", size=(20, 10), background_color='lightgray'), sg.Text("", size=(15, 1)), sg.Text("End Month       ", text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-STATE-", size=(15, 1), background_color='lightgray')],
    #     [sg.Text("Collaboration Tool ID", pad=(10, 15),text_color="#024A86", font=('Arial', 12, "bold")), sg.Input(key="-COLABTOOL-", size=(20, 10), background_color='lightgray')],
    #     [sg.Text("", size=(57, 1)), sg.Button("Update", size=(10,2), button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Text("", size=(10, 1)), sg.ButtonMenu('Reconciling Item', menu_def,  key='-Button_Menu-', button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"), size=(20,1))],
    #     [sg.Text("", pad=(10, 10))],
    #     # [sg.Image("Sin título.png", size=(250,250))],
    #     [sg.Button("OK", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold")), sg.Button("Exit", button_color=("#024A86", "#ccffff"), font=("Arial", 12, "bold"))]
    #     ]
    
    # return layout_tres

window = sg.Window("Main Menu", layout_main(),size=(800,500), resizable=True)





while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        
        break

    if event == "Admin Functions":

        window.close()
        window = sg.Window("BISAM", layout_admin(), size=(1500, 900), resizable=True)

    if event == "Go back":

        window.close()
        window = sg.Window("Main Menu", layout_main(),size=(800,500), resizable=True)

    if event == "OK":

        # window = sg.Window("Main Menus", layout_tres(),size=(1500, 900), resizable=True)
        state=str(values['-STATE-'])
        items=str(values['-ITEMS-'])
        status=str(values['-STATUS-'])

        data = [sublista for sublista in data if sublista[2][0] == 'kacmaz']
        # data = [[[elemento.replace('a', '') if isinstance(elemento, str) else elemento for elemento in sublista] for sublista in lista_externa] for lista_externa in data]
        # for lista_externa in data:
        #     for sublista in lista_externa:
        #         for i, elemento in enumerate(sublista):
        #             if isinstance(elemento, str):
        #                 sublista[i] = elemento.replace('a', '')

        window["-TABLE-"].update(values=data)

    if event == "Update":

        data=[]
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

        if selected_menu == 'Filed Claim':    
            print('a')
        elif selected_menu == 'Unfiled Claim':
            print('b')
        elif selected_menu == 'Refund Collected':
            print('c')
        elif selected_menu == 'Deposit':
            print('d')
        elif selected_menu == 'Next Return':
            print('e')
        elif selected_menu == 'Amend':
            print('f')
        elif selected_menu == 'Other Jur Return':
            print('g')
        elif selected_menu == 'TPP':
            print('h')
        elif selected_menu == 'Taxability Issue':
            print('i')

window.close()