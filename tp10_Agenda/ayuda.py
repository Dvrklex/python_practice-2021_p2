#leeer horariosssssssssssss
# import json
# with open('horarios.json') as contenido:
#     horarios = json.load(contenido)
#     for e in horarios: 
#             dia = e.get('Dia')
#             materias = e.get('Materias')
#             horas = e.get('Horarios')
#             priMat = materias[0]
#             segMat = materias[1]
#             priHora = horas[0]
#             segHora = horas[1]
#             show = '        >> '+dia+' <<'+'\n'+' - '+ priMat + ' de '+ priHora+ ' \n '+ '- '+segMat +' de ' + segHora+'.'
#             print(show)

############################################################
# file = open('notas.txt', 'r') #ver notasssss
# notas = file.readlines()
# notas.pop(0)
# file.close()
# for nota in range (len(notas)):
#     delSalto = notas[nota][:-1]
#     separar = delSalto.split(',')
#     salida = '> ' + separar[0] + ' --> ' + separar[1]
    # print(salida) 
# addfile = open('notas.txt', 'a')
# addNote = input('> Escriba la nueva nota: ')
# addfile.writelines(addNote+',pendiente'+'\n')
# addfile.close()
# file = open('notas.txt', 'r') #ver notasssss
# notas = file.readlines()
# print(notas)
# def seeNotes (notas):#ver notas 
#     for nota in range (len(notas)):
#         delSalto = notas[nota]
#         separar = delSalto.split(',')
#         salida = str(nota)+'> ' + separar[0] + ' --> ' + separar[1]
#         print(salida) 
# notasPersonales = ['Limpiar la PC,pendiente',
#     'Comprar comida para perro,pendiente',
#     'Refactorizar funciones,pendiente',
#     'Ir al banco,completa','Terminar boceto,pendiente','Hacer cacao,completa',
#     'Nota para eliminar1, pendiente','Nota para eliminar2, pendiente']  
# notPos = False
# seeNotes(notasPersonales)
# while not notPos:     
#     notePos = int(input('> Ingrese el numero de la nota a eliminar: '))
#     for eliminar in range (len(notasPersonales)):
#         if notePos == eliminar:
#             notasPersonales.pop(notePos)
#     seeNotes(notasPersonales)
#     notPos = True

# file = open('examenes.txt','r')
# leer = file.readlines()
# file.close()
# p = int(input('Ingrese una pos: '))
# newfile = open('examenes.txt','w')

# for e in range (len(leer)): 
#     if p != e: 
#         newfile.write(leer[e])