#!/usr/bin/env python
import PySimpleGUI as sg
import csv

# Show CSV data in Table
sg.theme('Dark Red')

def table_example():
    filename = sg.popup_get_file('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
    button = sg.popup_yes_no('Este archivo tiene numeros de columnas?')
    if filename is not None:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            if button == 'Yes':
                header_list = next(reader)
            try:
                data = list(reader)  
                if button == 'No':
                    header_list = ['Columna' + str(x) for x in range(len(data[0]))]
            except:
                sg.popup_error('Error al leer archivo')
                return
    sg.set_options(element_padding=(0, 0))

    layout = [[sg.Table(values=data,
                key='-AUTO-',
                headings=header_list,
                max_col_width=25,
                auto_size_columns=True,
                justification='right',
                change_submits=True,
                bind_return_key=True,
                enable_events=True,
                num_rows=min(len(data), 20))],
                [sg.Button('Datos'),sg.Button('Eliminar'),sg.Button('Modificar'),sg.Button('Salir',button_color='red')]           
                            ]


    window = sg.Window('Table', layout)
    
    
    while True:
        event, values = window.read()
        if event in [None, 'Salir']:
            break
        elif event == 'Datos':
            print(values[0])
            # valor = values[0].split(',')
            # salidaDatos = ' Propietario: ' + valor[0] + '\n\r' + 'Modelo: ' + valor[1]  + '\n\r' + 'Antiguedad: ' +valor[2] 
            # sg.popup('Datos seleccionados',salidaDatos)
        # elif event == 'Eliminar':
        #     valor = values['-AUTO-'][0].split()
        #     d.remove(values['-AUTO-'][0])
        #     print(values['-AUTO-'][0])
        #     print(d)
    window.close()
table_example()
