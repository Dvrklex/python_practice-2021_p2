prueba = 'Willa,1998-12-21 07:13:10'
posComa = prueba.find(',')
posGuion = prueba.find('-')
fec = prueba[posGuion-4:posGuion ]
mes = prueba[posGuion+1:posGuion+3]
dia = prueba[posGuion+4:posGuion+6]
name = prueba[:posGuion-5]
nacVerano = 'nada'
if int(fec) >= 1980 and int(fec) <= 1999:
            if (int(mes) >= 1 or int(mes) <= 3) or (int(mes) == 12):
                if int(mes) == 1:
                    if int(dia)>= 1 and int(dia)<= 31:
                        nacVerano = name + '\r'
                elif int(mes) == 2:
                    if int(dia)>= 1 and int(dia)<= 29:
                        nacVerano = name + '\r'
                elif int(mes) == 3:
                    if int(dia)>= 1 and int(dia)<= 20:
                        nacVerano = name + '\r'
                elif int(mes) == 12:
                    if int(dia)>= 21 and int(dia)<= 31:
                        nacVerano = name + '\r'       
print(name,fec,mes,dia) 
# for x in read:     
#         posGuion = x.find('-')
#         fec = x[posGuion-4:posGuion ]
#         mes =x[posGuion+1:posGuion+3]
#         dia =x[posGuion+4:posGuion+6]
#         name =x[:posGuion-5]   
#       if int(fec) >= 1980 and int(fec) <= 1999:
        #         if (int(mes) >= 1 or int(mes) <= 3) or int(mes) == 12:
        #             if int(mes) == 1:
        #                 if int(dia)>= 1 and int(dia)<= 31:
        #                     print('- ',name,'\r')
        #             elif int(mes) == 2:
        #                 if int(dia)>= 1 and int(dia)<= 28:
        #                     print('- ',name,'\r')
        #             elif int(mes) == 3:
        #                 if int(dia)>= 1 and int(dia)<= 20:
        #                     print('- ',name,'\r')
        #             elif int(mes) == 12:
        #                 if int(dia)>= 21 and int(dia)<= 31:
        #                     print('- ',name,'\r')     
        