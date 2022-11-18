from fuimba import inputInt, backTomenu, subrayar,todaysDate,makeMenu
import json
from datetime import date
notasPersonales = ['Limpiar la PC,pendiente',
'Comprar comida para perro,pendiente',
'Refactorizar funciones,pendiente',
'Ir al banco,completa','Terminar boceto,pendiente',
'Nota para eliminar1, pendiente','Nota para eliminar2, pendiente']
def mainMenu():
    subrayar()
    print('   >> AgendaNeitor v1.0 << ')
    makeMenu(op1 = 'Exámenes.',op2='Horarios de clases.',op3='Fecha de hoy.',op4='Notas personales.')
    print('0> Salir.')
    subrayar()
def showMenuExam ():
    subrayar()
    print('    > Examenes <')
    makeMenu(op1= 'Ver examenes.',op2='Eliminar examen.',op3='Agregar examen.')
    print('0> Volver al Menu Principal.')
    subrayar()
def showNotesMenu ():
    subrayar()
    print('    > Notas < ')
    makeMenu(op1='Ver notas.', op2='Agregar nota.',op3='Eliminar nota.')
    print('0> Volver al Menu Principal.')
    subrayar()

def seeExam(): #ver los examenes
    subrayar()
    file = open('examenes.txt','r')
    all = file.readlines()
    all.pop(0)
    for examen in range (len(all)):
        delSalto = all[examen][:-1]
        separar = delSalto.split(',')
        salida = '.'+ str(examen+1)+ '> ' + separar[0] + ' --> ' + separar[1]
        print(salida) 
    subrayar()
    backTomenu()
def addExam(): #añadir examanes 
    subrayar()
    addfile = open('examenes.txt', 'a')
    addExame = input('> Escriba la nueva nota: ')
    addfile.writelines(addExame+',pendiente'+'\n')
    addfile.close()
    subrayar()
    backTomenu()
def delExam():#eliminar un examen
    subrayar()
    seeExam()
    file = open('examenes.txt','r')
    leer = file.readlines()
    file.close()
    val = False
    while not val:
        posExam = inputInt('> Ingrese una posicion del examen a eliminar: ')
        if posExam > 0 and posExam < len(leer):
            newfile = open('examenes.txt','w')
            for e in range (len(leer)): 
                if posExam != e: 
                    newfile.write(leer[e])
            newfile.close()
            val = True
        else:
            print('Posicion no encontrada.')
    subrayar()
    backTomenu()

def seeNotes (notas):#ver notas 
    subrayar()
    for nota in range (len(notas)):
        delSalto = notas[nota]
        separar = delSalto.split(',')
        salida = '.'+str(nota)+' > ' + separar[0] + ' --> ' + separar[1]
        print(salida) 
    subrayar()
    backTomenu()
def addNotes (addNota):#agregar notas 
    subrayar()
    addNote = input('> Escriba la nueva nota: ')
    addNota.append(addNote+',pendiente'+'\n')  
    subrayar()
    backTomenu() 
def delNotes (delNota):#eliminar notas
    subrayar() 
    notPos = False
    seeNotes(notasPersonales)
    while not notPos:     
        notePos = inputInt('> Ingrese el numero de la nota a eliminar: ')
        for eliminar in range (len(delNota)):
            if notePos == eliminar:
                notasPersonales.pop(notePos)
        notPos = True
    subrayar() 
    backTomenu()
    
def seeHorarios(): #mostar los horarios
    subrayar()
    with open('horarios.json') as contenido:
        horarios = json.load(contenido)
        for e in horarios: 
                dia = e.get('Dia')
                materias = e.get('Materias')
                horas = e.get('Horarios')
                priMat = materias[0]
                segMat = materias[1]
                priHora = horas[0]
                segHora = horas[1]
                show = '              >> '+dia+' <<'+'\n'+' - '+ priMat + ' de '+ priHora+ ' \n '+ '- '+segMat +' de ' + segHora+'.'
                print(show)
                print()
    subrayar()
    backTomenu()
valid = False
while not valid:
    mainMenu()
    opMenu = inputInt('>> Ingrese una opción del Menu: ')
    if opMenu == 1: 
        examVal = True
        while examVal:            
            showMenuExam()            
            examOp = inputInt('>> Ingrese una opción del Menu: ')
            if examOp == 1:                 
                seeExam()                               
            elif examOp == 2:                
                delExam()                
            elif examOp == 3:                 
                addExam()                
            elif examOp == 0: 
                examVal = False
            else:
                print('Opción incorrecta.')     
    elif opMenu ==2: 
        seeHorarios()        
    elif opMenu ==3:
        print('   > La fecha de hoy es <')
        todaysDate() 
        backTomenu()      
    elif opMenu ==4: 
        notesVal = True
        while notesVal:            
            showNotesMenu()           
            noteOp = inputInt('>> Ingrese una opción del Menu: ')
            if noteOp == 1:                 
                seeNotes(notasPersonales)                              
            elif noteOp == 2:                
                addNotes(notasPersonales)                              
            elif noteOp == 3:               
                delNotes(notasPersonales)
            elif noteOp == 0: 
                notesVal = False
            else:
                print('Opción incorrecta.')
    elif opMenu==0: 
        valid = True
    else:
        print('Opción incorrecta.')

if __name__ == '__main__':
    print()
    # showMenu()  #mostrar menu principal
    # showMenuExam() #mostrar menu de examenes
    # seeExam() #mostrar examenes
    # delExam() #eliminar examenes
    # addExam() #añadir examenes
    # showNotesMenu() #mostrar menu de notas personales
    # seeNotes(notasPersonales) #mostrar notas personales
    # addNotes(notasPersonales) #añadir notas personales
    # delNotes(notasPersonales) #eliminar notas personales
    # seeHorarios() #mostrar los horarios