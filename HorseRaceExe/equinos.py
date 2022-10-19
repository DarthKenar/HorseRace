from cmath import exp
import random
import sys
class Equino:

    nombre_listas = "ColaNegra Picardo MetroFaist DestructorDeYeguas TrotaMundos PerroMaldito SecuazNegro Cimarrón DeserticoPalurdo Rabanito Cleopatrico ElMontés Amigo Chaparrón DienteDeHierro Velocirraptor".split()
    tipo_listas = ["PuraSangre", "CuartodeMilla", "Árabe", "Apalusa", "Andalúz", "Tennesseewalking", "Morgan"]
    

    def __init__(self, nombre = None, tipo = None, edad = None, velocidad = None, resistencia = None, nivel = None, precio = None):

        self.nombre = nombre
        self.nivel = nivel
        self.edad = edad
        self.tipo = tipo
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.precio = precio
        

    def __str__(self):

        atributos = [self.nivel,self.nombre,self.tipo,self.edad,self.velocidad,self.resistencia,self.precio,]
        atributos_cadena = ""
        print(f"""
Equino generado:
            Nivel: {self.nivel}
            Nombre: {self.nombre}
            Tipo: {self.tipo}
            Edad: {self.edad}
            Velocidad: {self.velocidad}
            Resistencia: {self.resistencia}
            Precio: {self.precio}
            """)
        for atributo in atributos:

            
            atributos_cadena = atributos_cadena + " " + str(atributo)

        return atributos_cadena[1:]

    def actualizar_nivel(self): #Metodo compartido para saber nivel del equino
        
        puntos = 0

        #Puntos por edad
        if self.edad in [1, 29, 30, 31, 32, 33, 34, 35]:
            puntos += 0
        elif self.edad in [2, 27, 28]:
            puntos += 1
        elif self.edad in [3, 4, 25, 26]:
            puntos += 2
        elif self.edad in [5, 6, 22, 23, 24]:
            puntos += 3
        elif self.edad in [7, 8, 9, 19, 20, 21]:
            puntos += 4
        elif self.edad in [10, 11, 12, 16, 17, 18]:
            puntos += 5
        elif self.edad in [13, 14, 15]:
            puntos += 6
        
        
        #puntos por velocidad
        if self.velocidad in range(15,25):
            puntos += 0
        elif self.velocidad in range(26,35):
            puntos += 1
        elif self.velocidad in range(36,45):
            puntos += 2
        elif self.velocidad in range(46,55):
            puntos += 3
        elif self.velocidad in range(56,65):
            puntos += 4
        elif self.velocidad in range(66,75):
            puntos += 5
        elif self.velocidad in range(76,85):
            puntos+= 6
        
        #puntos por resistencia
        if self.resistencia in [10]:
            puntos +=  0
        elif self.resistencia in [9]:
            puntos += 1
        elif self.resistencia in [8, 7]:
            puntos += 2
        elif self.resistencia in [6, 5]:
            puntos += 3
        elif self.resistencia in [4, 3]:
            puntos += 4
        elif self.resistencia in [2]:
            puntos += 5
        elif self.resistencia in [1]:
            puntos += 6
        
        #saca el promedio de puntos para ver el nivel del equino
        puntos = round(puntos/3)
        return puntos
        


    #Genera un equino aleatorio
    
    def generar_equino(self):
        
        self.nombre = random.choice(self.nombre_listas)
        self.edad = random.choice(range(1,35))
        self.tipo = random.choice(self.tipo_listas)
        self.velocidad = random.choice(range(15,86))
        self.resistencia = random.choice(range(1,10))

        #realiza un llamamiento al metodo actualizar nivel para determinar el nivel del equino generado aleatoriamente
        self.nivel = self.actualizar_nivel()

        #determina el precio según el nivel
        if self.nivel == 0:
            self.precio = random.choice(range(10000,30000))
        elif self.nivel == 1:
            self.precio = random.choice(range(30000,50000))
        elif self.nivel == 2:
            self.precio = random.choice(range(50000,70000))
        elif self.nivel == 3:
            self.precio = random.choice(range(70000,90000))
        elif self.nivel == 4:
            self.precio = random.choice(range(90000,110000))
        elif self.nivel == 5:
            self.precio = random.choice(range(110000,150000))
        elif self.nivel == 6:
            self.precio = random.choice(range(150000,200000))

    #El staticmethod sirve para poder utilizar el metodo sobre la instancia de la clase sin pasarle self
    @staticmethod
    def leer_equinos():

        archivo = open("equinos.txt", "r")
        archivo.seek(28) # serían 26 pero cuenta con el \n
        lineas = archivo.readlines()
        archivo.close()
        
        for line in lineas:

            lista =  line.split()
            print(f"Nivel: {lista[0]}\n Nombre: {lista[1]}\n Edad: {lista[2]}\n Tipo: {lista[3]}\n Velocidad: {lista[4]}\n Resistencia: {lista[5]}\n Precio: {lista[6]}\n")

    
    def guardar_equino(equino):

        equino_str = str(equino) + "\n"
        archivo = open("equinos.txt", "a")
        archivo.write(equino_str)
        archivo.close()

class Usuario:

    nivel = 0
    exp = 0

    def actualizar(self, experiencia_adquirida = None):

        self.exp += experiencia_adquirida

        if self.exp >= 100:
            
            self.nivel += 1
            self.exp = 0



if sys.__name__ == "__main__":
        
    #instanciamos al equino
    a = Equino()

    #generamos los atributos del equino
    a.generar_equino()

    #mostramos al hermoso equino de carreras
    print(a)
