from fuimba import inputInt, backTomenu,subrayar,makeMenu
file = open('cabins.csv','r')
read = file.readlines()
read.pop(0)
file.close()
numCabaña = []
reservas= []
persPcabaña = []
precios = []
entradaP = []
salidaP = []
for e in read: #obtener datos de las cabañas
    delSalto = e[:-1]
    separar = delSalto.split(',')     
    precios.append(int(separar[2][1:]))
    reservas.append(separar[3])
    persPcabaña.append(int(separar[1]))
    numCabaña.append(int(separar[0]))
    entradaP.append(separar[4])
    salidaP.append(separar[5])
for vacio,buscar in enumerate(entradaP) :#obtener fecha de entrada y salida de reservas
    if buscar == '':
        entradaP[vacio] = 'Vacio'
        salidaP[vacio] = 'Vacio'
        
def viewMenu ():
    subrayar()
    print('        >> Cabañas <<')
    makeMenu(op1='Mostrar datos de las cabañas.',op2='Mostras cabañas disponibles.',op3='Mostrar rango de precios.')
    print('0> Salir.')
    subrayar()
def datosCabañas():
    subrayar()
    print('Nº, Pasajeros, Precio, Reservada, In, Out.')
    for dato in range (len(numCabaña)):
        datos = str(numCabaña[dato])+'> '+str(persPcabaña[dato])+', $'+str(precios[dato])+', '+reservas[dato]+', '+entradaP[dato]+', '+salidaP[dato] +'.'
        print(datos)
    subrayar()
    backTomenu()
def cabañasDisponibles():
    subrayar()
    valCpersonas = False
    while not valCpersonas:
        cPersonas = inputInt('>> Ingrese cantidad de personas entre 2 y 4: ')
        if cPersonas >=2 and cPersonas <=4:
            valCpersonas = True
        else: 
            print('No respeta el límite.')
    subrayar()
    print('> Cabañas disponibles para',cPersonas,'personas:')
    for disponible in range (len(numCabaña)):
        if cPersonas == persPcabaña[disponible] and reservas[disponible] == 'no':    
                print('- Cabaña Nº:',str(numCabaña[disponible]))               
    subrayar()
    backTomenu()
def preciosCabañas():
    subrayar()
    print('----------------------------------')
    print('  Nº Cabaña  | Personas | Precio') 
    print('----------------------------------')
    for precio in range (len(numCabaña)):
        if numCabaña[precio] < 10:
            monto = 'Cabaña Nº '+ str(numCabaña[precio]) +'  |    '+ str(persPcabaña[precio])  +'     | $'+  str(precios[precio])  
            print(monto)
        else:
            monto = 'Cabaña Nº '+ str(numCabaña[precio]) +' |    '+ str(persPcabaña[precio])  +'     | $'+  str(precios[precio])  
            print(monto)
    print('----------------------------------')
    subrayar()
    backTomenu()
validado = True
while validado: 
    viewMenu()
    opcion = inputInt('>> Seleccione una opción del Menu: ')
    if opcion == 1:
        datosCabañas()        
    elif opcion == 2:
        cabañasDisponibles()      
    elif opcion == 3: 
        preciosCabañas()
    elif opcion == 0: 
        validado = False
    else: 
        print('Opción incorrecta. ')

if __name__ == '__main__':
    print()
    # datosCabañas()
    # cabañasDisponibles()
    # preciosCabañas()