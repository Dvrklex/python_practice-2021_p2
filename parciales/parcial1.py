remeras = [
   {'talle': 'S', 'colores': {'rojo': 4, 'verde': 2, 'azul': 0, 'blanco': 1}},
   {'talle': 'M', 'colores': {'rojo': 7, 'verde': 1, 'azul': 3, 'blanco': 7}},
   {'talle': 'L', 'colores': {'rojo': 2, 'verde': 0, 'azul': 4, 'blanco': 4}},
   {'talle': 'XL', 'colores': {'rojo': 3, 'verde': 5, 'azul': 7, 'blanco': 2}}
]

#punto 1 inicio
for cero  in range(len(remeras)):
    c_colores =  remeras[cero]['colores']
    for color,cantidad in c_colores.items():
        if cantidad == 0:
            salida = 'Faltantes:'+'<'+remeras[cero]['talle']+ ' '+color+'>'
            print(salida) #punto 1 
print()    
#punto  2 inicio
coloresRemeras = {}
for cero  in range(len(remeras)):
    c_colores =  remeras[cero]['colores']
    for co, cant in c_colores.items():
        if co not in coloresRemeras.keys():
            coloresRemeras[co] = cant
        else:
            coloresRemeras[co] += cant
minimo = min(coloresRemeras.values())
for color,menor in coloresRemeras.items():
    if menor == minimo:
        print('> Colores con menos unidades: ',color) #punto 2
print()
#punto 3 inicio
print('Remeras con mayor stock por talle y color:')
for cero  in range(len(remeras)):
    c_colores =  remeras[cero]['colores']
    for k,v in c_colores.items():
        if v == 7:
            print('> ',remeras[cero]['talle'],k,v)



# for x in range(len(remeras)):
#     colores = remeras[x]['colores']

#     for clave, valor in colores.items():
#         #print(clave, '->', valor)
#         if valor == mayor:
#             print("Remeras con mayor stock por talle y color:",mayor,talles,clave)
