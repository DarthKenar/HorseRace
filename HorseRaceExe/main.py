from io import *
from tkinter import E
from equinos import Equino

equino_generado = Equino()
equino_generado.generar_equino()

try:

    archivo = open("equinos.txt", "x")
    archivo.close()

    archivo = open("equinos.txt", "w")
    archivo.write("Lista de Equinos Generados\n")
    archivo.close()
    
except FileExistsError:

    print("El archivo ya existe")

#Equino.guardar_equino(equino_generado)
Equino.leer_equinos()




