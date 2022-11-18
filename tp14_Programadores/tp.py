# from fuimba import inputInt,valInt
import random
class Empleado():
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo  #si es python 175k sino 115k
    def getNombreySueldo(self):
        return self.nombre,self.sueldo

class Programador(Empleado):
    def __init__(self,nombre,sueldo,lenguaje):
        Empleado.__init__(self,nombre,sueldo)
        self.lenguaje = lenguaje

    def asignarProyecto(self):
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        numPro = int(random.randint(0,len(self.listaProyectos)-1))     
        return self.listaProyectos[numPro]
        
    def verDatos(self):#devolver proyecto y lenguaje
        return self.listaProyectos[self.asigPro],self.lenguaje

class Empresa():
    def __init__(self):      
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores = []

    def getNombreyRubro(self):#devolver nombre y rubro 
        return self.nombre,self.rubro

    def agEmp(self):
        res = 'si'
        while res.lower() == 'si':
            self.nLenguaje=input('Ingrese lenguaje que maneje: ')
            for i in self.listaLenguajes:
                if self.nLenguaje == i:
                    newEmpleado = input('Ingrese nombre: ')                    
                    if self.nLenguaje == 'Python': #sueldo de 175000                   
                        newProgramador = Programador(newEmpleado,175000,'Python') #composicion
                        self.listaProgramadores.append(newProgramador)
                    else:
                        newProgramador = Programador(newEmpleado,115000,self.nLenguaje) #composicion
                        self.listaProgramadores.append(newProgramador)
            res = input('Desea cargar mas datos: ')

    def mostrarTodo(self):
        for mostrar in self.listaProgramadores:
            print(f'{mostrar.getNombreySueldo()[0]}  - ${mostrar.getNombreySueldo()[1]} - {mostrar.lenguaje} - {mostrar.asignarProyecto()}  ')

   
loco1 = Empresa()

loco1.agEmp()
loco1.mostrarTodo()