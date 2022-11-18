#Solucion 2 
import json
from os import pipe  
def cargarDatos (ruta): 
    titles = [] #Titulos 
    actors = [] #Actores principales
    rottenTomatoes = [] #Ratings
    boxOffice = [] #Recaudaciones
    with open(ruta) as contenido:
        pel = json.load(contenido)
        #---------------------------------#
        ap = []  #Listas aux de actores.
        pa = []  #Listas aux de actores.
        names = [] #Listas aux de actores.
        #---------------------------------#
        c = 1
        values = []
        for x  in pel : 
            t = x.get('Title') #Obtener cada titulo
            titles.append(t)
            b = x.get('BoxOffice')  #Obtener las recaudaciones
            boxOffice.append(b) 
            ro = x.get('Ratings')  #Obtener ratings
            for val in ro:
                v = val.get("Value") #Obtiene los valores de los ratings
                values.append(v)
                for n in range(len(values)):
                    if n == c:
                        rottenTomatoes.append(values[n])
                        c += 3        
            #-----------------------------------------------------------
            a = x.get('Actors')  #Obtener actores principales de c/pelicula
            pa.append(a)
        for r in pa:
            posComa = r.split(',')
            ap.append(posComa)
            for sub in ap:
                for elim in range(len(sub)):
                    if elim == 0:
                        names.append(sub[elim])
                        actors = list(set(names))
                        actors.sort()
            #-----------------------------------------------------------                 
        escribir = ''  #Escribir en el archivo CSV
        csv = open('pelis.csv','w')
        formato = 'Nombre,   Actor,   Rating,   Recaudacion \r' 
        csv.writelines(formato)
        for i in range(len(titles)): 
            if rottenTomatoes[i] != '%' and boxOffice[i] !='$':
                escribir = titles[i] + ';' + actors[i] + ';' + str(rottenTomatoes[i]) +  ';' + str(boxOffice[i]) + '\r'
                csv.writelines(escribir)
        csv.close()
    return titles,rottenTomatoes,boxOffice,actors
if __name__ == '__main__':
    ruta = 'pelis.json'
    cargarDatos(ruta)