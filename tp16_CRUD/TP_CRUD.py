from fuimba import *
def aCSV ():
    archivo = open('datos.csv','r')
    leoArchivo = archivo.readlines()
    cabeceras = leoArchivo.pop(0)
    # print(leoArchivo)
    archivo.close()
    return cabeceras,leoArchivo
h,d = aCSV()

import PySimpleGUI as sg
sg.theme('black')
def filas(head,data):
    layout = [ [sg.Text(head)], 
            [sg.Listbox(values=data,
                size=(25,len(data)),
                key='-DATA-',
                change_submits=True,
                bind_return_key=True,
                enable_events=True)],                
                [sg.Button('Datos'),sg.Button('Agregar'),sg.Button('Eliminar'),sg.Button('Modificar'),sg.Button('Salir',button_color='red')]           
            ]
    return layout
def modFilas():
    filasMod = [
                        [sg.Text('Propietario'),sg.Input(key='nombre')],
                        [sg.Text('Modelo'),sg.Input(key='modelo')],
                        [sg.Text('Antiguedad'),sg.Input(key='antig')],
                        [sg.Text(size=(40,1),key='guardado')],
                        [sg.Button('Guardar')]                    
                    ]
    return filasMod
def addDatas(): 
    agregarData = [
        [sg.Text('Propietario'),sg.Input(key='addnombre')],
        [sg.Text('Modelo'),sg.Input(key='addmodelo')],
        [sg.Text('Antiguedad'),sg.Input(key='addantig')],
        [sg.Button('Guardar')]            
    ]
    return agregarData


window = sg.Window('Visor de Datos', filas(h,d)) 
while True:
    salidaDatos = ''
    addNewData = ''
    addData = ''
    valData = True
    valMod = True
    event, values = window.read()
    if event in [None, 'Salir']:
        break   
    
    elif event == 'Datos':
        valor = values['-DATA-'][0].split(',')
        salidaDatos = ' Propietario: ' + valor[0] + '\n\r' + 'Modelo: ' + valor[1]  + '\n\r' + 'Antiguedad: ' +valor[2] 
        sg.popup('Datos seleccionados',salidaDatos)

    elif event == 'Agregar':
        windowAdd = sg.Window('AGREGAR',addDatas()) 
        while valData: 
            e,v = windowAdd.read()
            valNum = verificarInt(v['addantig'])
            if valNum[0]:
                addData = v['addnombre']+','+v['addmodelo']+','+v['addantig']
                if e == 'Guardar':
                    d.append(addData)
                    valData = False
                    windowAdd.close()
            else:               
                sg.popup('Error','Debe ingresar un numero entero en Antiguedad')
        window['-DATA-'].update(d)
                            
    elif event == 'Eliminar':
        eliminar = values['-DATA-'][0]
        posiDel = d.index(eliminar)
        d.pop(posiDel)
        window['-DATA-'].update(d)

    elif event == 'Modificar':
        oldData = d.remove(values['-DATA-'][0])
        windowMod = sg.Window('MODIFICAR',modFilas())
        while valMod:
            evento,valoor = windowMod.read()
            valido = verificarInt(valoor['antig'])
            if valido[0]:
                if evento == 'Guardar':            
                    addNewData = valoor['nombre']+','+valoor['modelo']+','+valoor['antig']+'\n' 
                    d.append(addNewData)
                    window['-DATA-'].update(d)
                    valMod = False
            else:               
                sg.popup('Error','Debe ingresar un numero entero en Antiguedad')             
        windowMod.close()

window.close()

