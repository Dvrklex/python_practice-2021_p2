#SOLUCION 1
movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
    "Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
    "Three Kings(1999)act", "The green hornet(2011)com"]

genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}
pelisXgenero = []
pelisXletra = []
print('Tipos de generos:')
print('act = Accion')
print('sf = Ciencia Ficcion')
print('com = Comedia')
usu = input('Ingrese un genero teniendo en cuenta el menu anterior: ')
usu = usu.lower() 
c = 0
anioUsu = int(input('Anio: '))
letUsu = (input('Ingrese una letra: '))
letUsu = letUsu.upper()
for peli in movies:
    posiParent = peli.find('(')
    nombre = peli[:posiParent]
    anio = int(peli[posiParent + 1 : posiParent + 5])
    genero = peli[posiParent + 6:]
    if genero == usu:
        pelisXgenero.append(nombre)   
    if anio < anioUsu:
        c += 1
    if nombre[0] == letUsu:
        salida = nombre +'. Año: '+ str(anio) +'. Genero: '+ genre[genero]
        pelisXletra.append(salida)

print()
print('Las peliculas del genero ',genre[usu],' son')
for e in pelisXgenero : 
    print('-',e)
print()
print('Antes del año ',anioUsu,' fueron estrenadas ',c,' peliculas.')
print()
print('Peliculas que empiezan con la letra ',letUsu)
for e in pelisXletra : 
    print('-',e)