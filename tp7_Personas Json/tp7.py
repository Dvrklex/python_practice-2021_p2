from json import loads

file = open('practico7.json', 'r',encoding = 'UTF-8')
all = file.read()
file.close()
dic = loads(all)
###------------------
print(type(dic))
paises = {}
for e in dic:
    pais = e['location']['country']
    if pais not in paises.keys():
        paises[pais] = 1
    else:                       
        paises[pais] += 1

paises = dict(sorted(paises.items(), key=lambda x: x[1], reverse=True))
print('Personas por pais')
for k, v in paises.items():
    print(k, ":", v, 'personas')
print()
                                #cantidad de personas por pais
from collections import Counter
lang = []
for e in dic:
    lang.extend(e['languages'])
d = dict(Counter(lang))
maxi = max(d.values())

def getKeys(dic, value):
    return [key for key, val in dic.items() if val == value] #lista por comprencion para obtner las keys

print(maxi, 'personas hablan:')
for i in getKeys(d, maxi):
    print(i)          #Cantidad personas que hablan tal idioma