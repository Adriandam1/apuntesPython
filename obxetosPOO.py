import math


# definir clase en python class <nomeClase>: <propiedades>
class Punto:
    """Clase que define un punto bidimensional no primeiro cuadrante(necesito x e y)"""
    #iniciamos a clase co metodo init
    # seria como o constructor de java, pero non e o constructor, nos sirve para designar valores y hace referencia a si mismo(como en java this)
    def __init__(self, x=0, y=0): #no hace falta declarar el tipo de la variable por que python tiene tipado dinamico
        self.x = x
        self.y = y
    # tamen podemos facer metodos
    # os getters e setters son innecesarios en python
    # metodo que nos permite acceder a x
    def get_X (self):
        return self.x
    # metodo que nos permite acceder a y
    def get_Y(self):
        return (self.y)

    # el toString de java aqui seria
    def __str__(self):
        # print ("A coordenada x é: "+str(self.x)) # los atributos x e y estan creados en init, para hacer referencia a ellas teriamos que usar self
        # print ("A coordenada y é: "+str(self.y))
        # cambiamos el toString para la prueba de abajo
        return "A coordenada x é: "+str(self.x) + "\nA coordenada y é: "+str(self.y)

    # implementamos eq
    def __eq__(self, p2):
        if self.x == p2.x and self.y == p2.y:
            return True
        else:
            return False

    # como se crea un obxeto punto
p1 = Punto()
print (p1)
#con los property ahora podemos:
p1.x = 15
p1.y = -3
print (p1) # vemos que non se queixa

# vamos crear algun metodo que teñamos que facer mais para chamalo
print("A coordenada x é: "+str(p1.get_X()))
# tamen se poderia facer asi: (haria los getters inutiles, en java hacer falta, en python no)
print("A coordenada x é: "+str(p1.x))

#Herencia en Python pode ser multiple, o contrario que en Java
#Asi se declara en Python de forma sinxela:

#si heredase mas de una clase seria:
""" Ejemplo: 
class Circulo (Punto, Figuras):
"""

#Clase circulo vai heredar algo de punto
class Circulo (Punto):
    def __init__(self, x=0, y=0, r=0):
        Punto.__init__(self, x, y)
        self.r = r

    def perimetro (self):
        return 2*math.pi * self.r

    def area (self):
        return math.pi * math.pow(self.r,2)


    def __str__(self):
        return Punto.__str__(self) + "\nO radio é: " +str(self.r)

c1 = Circulo()
c1.x = 3
c1.r = 5
print (c1)
print ("O perimetro é: "+str(c1.perimetro()))

#Polimorfismo en Python, aqui es menos importante
#Encapsulacion en Python, la encapsulacion se trata de controlar y limitar el acceso a las clases, en python sin restriccion puede hacer cosas como las de arriba, invocar la variable y listo
#Para ocultar o que el acceso sea mas limitado vamos a crea una clase Punto2
# resumen la encapsulacion en python es una MIERDA

class Punto2:
    """Clase que define un punto bidimensional no primeiro cuadrante(necesito x e y)"""
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX (self):
        return self.__x
    def setX (self, x):
        if x > 0:
            self.__X = x
        else:
            x = 0
            print("O valor de x non pode ser negativo, iniciando x=0")

    def getY(self):
                return self.__y

    def setY(self, y):
        if y > 0:
            self.__Y = y
        else:
            y = 0
            print("O valor de y non pode ser negativo, iniciando y=0")
    #Podemos asignar para que cada vez que quiera recuperar el valor de la propiedad x getX, y cada vez que quiera aisgnar valor utilize setX
    x = property(getX, setX)
    #Lo mismo para y
    y = property(getY, setY)

    def __coordenadas (self):
        return "As coordenadas son: (" +str(self.__x)+ ',' +str(self.__y) +')'

    def __str__(self):
        return "A coordenada x é: "+str(self.__x) + "\nA coordenada y é: "+str(self.__y)

p2 = Punto2()
print(p2)
#print ("A coordenada x é: " +str(p2.x))
#print (p2.__coordenadas()) ## las coordenadas no son accesibles
#para acceder
print (p2._Punto2__coordenadas())

#comprobamos property en Punto2:
p2.x = 4
p2.y = -3
print(p2)

c1= Circulo()
c1.x = 3
c1.r = 5
print (c1)
print ("O perimetro é: "+str(c1.perimetro()))

"""
object
metodos de object:
__init__(self)
__str__(self)
__new__(class, args)
__del__(self) es el destructor, lo usaremos como recolector
__len__(self) lo usaremos en colecciones y lo llamaremos para saber la lonxitude dun obxeto
"""

#Metodos compare
p3 = Punto(2, 3)
p4 = Punto(2,3)
print (p3.__eq__(p4)) # resultado: NotImplemented tendriamos que facelo arriba declarar __eq__ en la clase Punto
#otra manera de facelo
print (p3 == p4)





