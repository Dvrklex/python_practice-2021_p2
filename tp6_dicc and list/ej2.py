#SOLUCION 2
movies =  ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
     "Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
     "Three Kings(1999)act", "The green hornet(2011)com"]
anio = int(input('Anio: '))
num = ''
c = 0
for numero in movies:
    for x in numero:
        if x in '0123456789':
            num += x      
num1 = list(num)             
for i in range(len(num1),0,-4):
    num1.insert(i,'-')
punto=''.join(num1)
fec = punto.split('-')
fec.pop(-1)
fec = list(map(int, fec))
for x in fec: 
    if x<anio:
        c = c + 1
print('Antes del año ',anio,' fueron estrenadas ',c)
