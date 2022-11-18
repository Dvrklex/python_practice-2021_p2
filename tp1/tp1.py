name = ["Ana Torres","Kate Hudson","Benicio Quesada","Susana Campoamores","Carlos Santamaria","Azul Skarsgard","Walter Catalejos"]
eliminar = ["na","ate","enicio","usana","arlos","zul","alter"]
a = (name[0].split(eliminar[0]))
b = (name[1].split(eliminar[1]))
c = (name[2].split(eliminar[2])) 
d = (name[3].split(eliminar[3])) 
e = (name[4].split(eliminar[4])) 
f = (name[5].split(eliminar[5])) 
g = (name[6].split(eliminar[6]))
t = ['  ']
nyi = a + t + b + t + c + t + d + t + e + t + f + t + g 
fi = ''
for e in range (len(nyi)):
    if nyi[e] != '""':
        fi = fi + nyi[e]
spl = fi.split('  ')
fuck = ','.join(spl)
newFuck = fuck.replace(' ','.')
namesLista = newFuck.split(',')
print('1)Iniciales y apellido de las personas:')
for i in range(len(namesLista)):
    print(namesLista[i])
#--------------------------------------------------------------------------
#saber cual es el nombre mas largo (Esta funcion puede ser reutilizada)
def encontrar_la_palabra_mas_larga(palabras):
    palabra_longitud = []
    for p in palabras:
        palabra_longitud.append((len(p),p))
    palabra_longitud.sort()
    return palabra_longitud[-1][1]
palabras = ['Ana','Kate','Benicio','Susana','Carlos','Azul','Walter']
print('2) El nombre mas largo es: ',encontrar_la_palabra_mas_larga(palabras))
#Calcular edad femenina promedio
from calcula_edad import edad
nacimiento =["02/05/1943","07/09/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
sexo=["f","f","m","f","m","f","m"]
if __name__ == '__main__':
    eM1=int(edad('02-05-1943'))
    eM2=int(edad('07-09-1984'))
    eM3=int(edad('21-12-1967'))
    eM4=int(edad('30-08-1995'))
promEdades = (eM1 + eM2 + eM3 + eM4) // 4
print('3) El promedio de edades es:',promEdades)