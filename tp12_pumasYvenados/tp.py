from fuimba import *
class Animal():
    def estado(self):
        pass
class Puma(Animal):
    def __init__(self,identificador,edad,peso):       
        self.identificador = identificador
        self.edad = edad
        self.peso = peso #sano 200 o mas
    def estado(self):
        if self.peso >= 200:
            return 'Sano'
        else:
            return 'Enfermo'
    def edadPuma (self):
        if self.edad > 5:
            return True
        else:
            return False

class Venado(Animal):
    def __init__(self,identificador,peso):
        self.identificador = identificador
        self.peso = peso   #sano 120 o mas
    def estado(self):
        if self.peso >= 120:
            return 'Sano'
        else:
            return 'Enfermo'
# ---------------------------------------------------------
class Jaula():
    def __init__(self,animal,cantidad):       
        self.jaula = []
        for x in range(cantidad):            
            peso = inputInt(f'Peso del {animal}: ')
            if animal == 'puma':
                edad = inputInt(f'Ingrese edad del {animal}: ')
                ani = Puma(x+1,edad,peso)
            else:
                ani = Venado(x+1,peso)
            self.jaula.append(ani)
        
    def cAdultos (self):
        self.c = 0
        for x in self.jaula:
            if x.edadPuma():
                self.c += 1
        print(f'Cantidad de pumas adultos: {self.c}')

    def mostrarJaula(self):
        c = 1
        for x in self.jaula:
            print(f'N° {c} - {x.estado()}')
            c+=1
if __name__ == "__main__":
    jaul = Jaula('puma',3)
    jaul.mostrarJaula()
    jaul.cAdultos()
    jaul = Jaula('venado',2)
    jaul.mostrarJaula()