#Solucion SALVAJE en 55 lineas.
file = open('pelis.json','r')
leo = file.readlines()
titulos = []
actores = []
porcentajes = []
recaudaciones= []
titu= []
act = []
por = []
rec = []
file.close()
pel = open('pelis.csv','w')
formato = 'Nombre' +';'+ 'Actor' +';'+ 'Rating' +';'+ 'Recaudacion' + '\n'
pel.writelines(formato)
for x in leo:
    if 'Title' in x:
        # print(x)
        titulos.append(x)
    if 'Actors' in x:
        # print(x)
        actores.append(x)
    if '%' in x:
        # print(x)
        porcentajes.append(x)
    if '$' in x:
        # print(x)
        recaudaciones.append(x)
for x in titulos:
    dosPuntos = x.find(':')
    posComa = x.find(',')
    ti = x[dosPuntos+3:posComa-1]   
    titu.append(ti)
    # print(ti)
for x in actores:
    posComa = x.find(',')
    ac = x[dosPuntos+4:posComa]
    act.append(ac)
    # print(ac)
for e in porcentajes:
    porcPosi = e.find('%')
    val = e[porcPosi-2:porcPosi]
    por.append(val)
    # print(val)
for p in recaudaciones:
    dosPuntos = p.find(':')
    re = p[dosPuntos+4:-3]
    rec.append(re)
    # print(re)
for w in range(len(titu)):
    escribir = titu[w] + ';' + act[w] + ';' + por[w] + ';' + rec[w] + '\n'
    pel.writelines(escribir)    
pel.close()