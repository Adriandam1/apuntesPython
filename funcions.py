
#Como se definen funcions en java(metodo)
#public void nomeMetodo (tipo1 parametro1, tipo2 parametro2...){ codigo}

#Como declaro en Python unha funcion:
#Non necesitamos indicar que parametro retornar, non necesitamos indicar o tipo de dato que chama
def nome_funcion (parametro1, parametro2):
    print (parametro1)
    print (parametro2)
#En python permite a execucion funcional, non necesitamos crear unha clase para usar o metodo
nome_funcion("Ola", " a todos")
nome_funcion(1, 3)

#co memos razonamento
def suma (operando1, operando2):
    print("A suma é: " +str(operando1+operando2))
suma(1, 3) #A suma é: 4
suma("un","tres") #A suma é: untres
#suma(1, "tres") # ROMPE

#EU poderia aignarlle un valor por defecto os elementos da funcion, neste caso o operando2
print ("Suma2")
def suma2 (operando1:int=0, operando2:int=0):
    print("A suma é: " +str(operando1+operando2))
suma2() # 0+0 = 0
suma2(1) # 1+0 = 1
suma2(8) # 8 + 0 =8
#Podemos eligir que cambiar
suma2(operando2=5)

#
def imprimir (texto="-", veces = 1):
    print (veces * texto)
imprimir("Ola", 5)
imprimir (5) # imprime texto (5) unha vez
imprimir (veces=5) #imprime texto 5 veces
imprimir (veces = 8, texto = "Peras") # imprime Peras 8 veces

# Podo definir unha funcion que teña un numero indefinido de parametros e non teña informacion deles
# O asterisco ya di a funcion que ten un numero indefinido de parametros
def variosParametros(parametro1, parametro2, *outros):
    print(parametro1, parametro2)
#Cos parametros que teña ahi crea unha tupla
    for parametro in outros:
        print(parametro)

variosParametros(4, 76)
#Podemos acceder a todos os parametros que queiramos, os parametros son anonimos
variosParametros(2,3,4,5,6,7,8,9,"hola")

#Poderiamos ter unha solucion para que tivesen nomes os parametros e desaxen de ser anonimos
def variosParametrosNonAnonimos (parametro1, parametro2, **outros):
    print(parametro1, parametro2)
    for clave in outros.keys():
        print(clave + " = " + str(outros[clave]))
variosParametrosNonAnonimos(1, 3, operando3 = 4, operando4 = 9, operando5 = 3)

def variosParametros2(*outros):
    for parametro in outros:
        print(parametro)
var = 1
#Con esto traballariamos co valor de var (1) pero non co a variable
variosParametros2 (var,3,4,5)

#Paso de parametro por valor e referencia

def funcion (a, b):
    a = a + 5
    b.append (23) # append engade un elemento mais a lista
    #Esto vai sumar 5 o elemento a, e o elemento b engadir lista
    print(a, b)
    #Se quixeramos retornar o valor de a teriamos:
    #return a
    #Se quisexemos returnar a e b:
    return a, b

a = 12 # creamos a que ten valor 12
b = [44] # creamos b que vai ten un elemento
c, d = funcion (a, b) #Retornamos o valor de a e b
funcion (a, b) #valor local na funcion
print (a, b) #valor global
print (c, d) #mostramos o valor retornado









