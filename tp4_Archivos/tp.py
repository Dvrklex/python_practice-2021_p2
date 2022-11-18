from os import write


file = open('deudores.txt', 'r',encoding = 'UTF-8')
all = file.readlines()
all.pop(0) 
file.close()
morosos = open('morosos.txt', 'w')
morosos.write('Nombre,  Mail,  Saldo\n')
for linea in all:
    deudor = linea.split(',')
    deuda = int(deudor[4][1:-3])
    anio = deudor[5][-4:]
    if deuda > 200000 and anio == '2019':
        w = deudor[1] + ';' + deudor[2] + ';' + str(deuda) + '\n'
        morosos.write(w)
morosos.close()
