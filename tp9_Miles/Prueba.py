import random
from fuimba import valInt


rangoN= '1'
while (len(set(rangoN))) != 4:
    rangoN = str(random.randint(1000, 9999))

adivinado = False
while not adivinado:
    print(rangoN)
    usuNum = str(valInt('Ingrese un numero: ', min = 1000, max = 9999))
    if usuNum == rangoN:
        print('aca hay una coincidiencia') 
        adivinado = True



# from tkinter import Tk, Label, Button
# class VentanaEjemplo:
#     def __init__(self, master):
#         self.master = master
#         master.title("Una simple interfaz gráfica")
#         self.etiqueta = Label(master, text="Esta es la primera ventana!")
#         self.etiqueta.pack()
#         self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
#         self.botonSaludo.pack()
#         self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
#         self.botonCerrar.pack()
#     def saludar(self):
#         print("¡Hey!")
# root = Tk()
# miVentana = VentanaEjemplo(root)
# root.mainloop()