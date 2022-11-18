#Reformulen la solución utilizando almacenamiento en archivo de texto. Para ello:
#1) Escriban un programa de carga, 
# que tome los datos solicitados al usuario y 
# los almacene en un archivo de texto en el formato que prefieran. 
# Pueden previamente almacenarlos en listas o no, es opcional.
from os import close
def inputPersonas(name, fecha):
    nombresLista = []
    fecNac = []
    c = int(input('Cuantas personas desea cargar?: '))
    for x in range(c):  
        name = input('Ingrese un nombre: ') 
        nombresLista.append(name)
        fecha = input('Ingrese fecha de nacimiento (ej: 01-01-2001): ')
        fecNac.append(fecha)
    
    return nombresLista, fecNac

nombres,fechas = inputPersonas('Ingrese nombre \n','Ingrese fecha de nacimiento (ej:02-02-2002): \n')

archivo = open('tp3.txt','w')
archivo.write('nombres=%s \n'%nombres)
archivo.write('fechas=%s \n'%fechas)
#--------FUNCION DE CARGA CON TXT COMO PARAMETRO-----------
#def inputPersonas(name, fecha,archivo=open(tp3.txt,'w')):
#    nombresLista = []
#    fecNac = []
#    c = int(input('Cuantas personas desea cargar?: '))
#    for x in range(c):  
#        name = input('Ingrese un nombre: ') 
#        nombresLista.append(name)
#        archivo.write(name)
#        fecha = input('Ingrese fecha de nacimiento (ej: 01-01-2001): ')
#        fecNac.append(fecha)
#        archivo.write(fecha=%s \n'%fecha)           
#   return nombresLista, fecNac
#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
#2) Escriban un segundo programa que tendrá como 
# salida los nombres de los mayores de edad. 
# Para ello, deberán leer el archivo creado en el punto 1 
# y reutilizar la o las funciones que hayan escrito para la salida original.

archivo = open('tp3.txt','r')
todo = archivo.read()

archivo.close()
from calcula_edad import edad
print('Las personas mayores de edad son: ')
for x in range(len(nombres)):
    if edad(fechas[x]) >= 18:
        print(nombres[x], 'con', edad(fechas[x]))
