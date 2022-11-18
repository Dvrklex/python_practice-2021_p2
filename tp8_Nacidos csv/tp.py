file = open('nacidos.csv','r')
read = file.readlines()
read.pop(0)
añoUsu = input('Ingrese un año entre 1980 y 1999: ')
pers = []
for x in read:     
        posGuion = x.find('-')
        fec = x[posGuion-4:posGuion ]
        mes =x[posGuion+1:posGuion+3]
        dia =x[posGuion+4:posGuion+6]
        name =x[:posGuion-5]
        if añoUsu == fec:
            if int(mes) == 1:
                    if int(dia)>= 1 and int(dia)<= 31:
                            pers.append(name)
            elif int(mes) == 2:
                    if int(dia)>= 1 and int(dia)<= 28:
                            pers.append(name)
            elif int(mes) == 3:
                    if int(dia)>= 1 and int(dia)<= 20:
                            pers.append(name)
            elif int(mes) == 12:
                    if int(dia)>= 21 and int(dia)<= 31:
                            pers.append(name)     
print('Las personas nacidas en el veranos son: ')
for  i in pers:
    print('-',i,'\r')