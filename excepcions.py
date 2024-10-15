import math

# INICIAMOS EXCEPCIONS
#Para lanzar excepciones usamos clase exception onde se basarian cando creamos a execepcion, serian o marco ou clase da que heredan todas as excepcions
#Lo que en java es try-catch en Python es try-except


#Xeneramos a nosa excepcion:
class NonPrimeiroCuadranteError(Exception):
    def __str__(self):
        return "Erro de coordenadas fora do 1º cuadrante."
#Exemplo manuel:
"""
try:
    p2 = Punto2()
    p2.x = 4
    p2.y = -3
except NonPrimeiroCuadranteError as e:
    print ("Erro no programa: "+e.__str__())
    print(e)
print (p2)
"""






















