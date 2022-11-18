import random
from fuimba import valInt
def genNum():
    rangoN= '1'
    while (len(set(rangoN))) != 4:
        rangoN = str(random.randint(1000, 9999))
    return rangoN

numPc = genNum()

print(numPc,'este es',len(numPc))
cIntentos = 0
win = False
while not win:
    regular = 0
    bien = 0 
    user = str(valInt('Ingrese un numero entre (1000-9999): ',min=1000,max=9999))
    cIntentos += 1
    for buscar in range(4):               
        if user[buscar] in numPc:           
            if user[buscar] == numPc[buscar]:
                bien += 1 
            else: 
                regular += 1 
    if bien == 4:
        win = True
        print('Has ganado, el numero era:',numPc)
        print(f'Intentos:{cIntentos}')
    else: 
        print(f'Bien = {bien}')
        print(f'Regular = {regular}')

nickName = input('Ingrese nombre: ')
file = open('Rankings.txt','a')
file.writelines(nickName +'='+ str(cIntentos) + '\r' )
file.close()

infinite = 1e309

leer = open('Rankings.txt','r')
leerFile = leer.readlines()
top1 = infinite
top2 = infinite
top3 = infinite
nombrer1 = ''
nombrer2 = ''
nombrer3 = ''
for x in leerFile:
    iwal = x.find('=')
    salto = x.find('\n')
    numero = x[iwal+1:salto]
    numero = int(numero)
    nombre = x[:iwal]
    if numero < top1:
        top2 = top1
        top1 = numero
        nombrer2 = nombrer1
        nombrer1 = nombre
    elif numero > top1 and numero < top2 or numero == top1:
        top3 = top2
        top2 = numero
        nombrer3 = nombrer2
        nombrer2 = nombre
    elif numero > top2 and numero < top3 or numero == top2:
        top3 = numero
        nombrer3 = nombre

print('RANKING JUGADORES TOP 3')
print('Nombre','       ','Intentos')
print(nombrer1,'            ',top1)
print(nombrer2,'            ',top2)
print(nombrer3,'            ',top3)

