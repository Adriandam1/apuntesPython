
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

# 8/10/24
#Printeamos funciones dentro de funciones y probamos llamadas
def saudar (lingua):
    def saudar_en():
        print("Hi")
    def saudar_fr():
        print('Salut')
    def saudar_gl():
        print('Ola')
    def saudar_es():
        print('Hola')

    lingua_func = {"es": saudar_es, "gl": saudar_gl, "fr": saudar_fr, "en": saudar_en}

    return lingua_func[lingua]
saudoEspanol = saudar('es')
saudoEspanol() # sacaria "Hola"
saudar('en')() # sacaria "Hi"
print (saudar('es')) # sacaria "<function saudar.<locals>.saudar_es at 0x7fca66987420>"

# As funcions Lambda
#as funcions lambda serian as funcions anonimas, funcions o metodos que non ten nome, serian de usar y tirar,
# osea serian para aforrar tanto que no espacio de nomes a etiqueta que poñemos esto e tan rata que xa nin queremos
# tener nome para non ter esa referencia cruzada, seria como esa maquinilla desechable
# ten unha limitacion, son tan escuetas que so admiten unha instruccion, o minimo do minimo


def cadrado (n):
    return n**2
# "vou a explicar compresion de listas"
lista = [-2,-1,0,1,2,3,4]

#creo unha nova lista onde o valor de cada elemento va a ser o valor de num*2 onde num e cada elemento de lista
novaLista =[num*2 for num in lista]
#unha nova lista onde cada elemento de esta lita vai a ser o cadrado de n onde n e cada elemento de esta lista
novaLista2 =[cadrado (n) for n in lista]
#Filtra os elementos da lista que son maior que 0
novaLista3 = [n for n in lista if n>0]
#Poderian combinarse as 3 cousas para manipular ou transformar a lista de moitas maneras
novaListaCombinada = [cadrado(num * 2) for num in lista]
# Funcion lambda, funcion de uso rapido de usar y tirar
novaLista4 = [(lambda n : n**2)(n) for n in lista]

# Resultado das listas:
print("Lista original:", lista)
print("Nova Lista (cada elemento * 2):", novaLista)
print("Nova Lista 2 (cadrado de cada elemento):", novaLista2)
print("Nova Lista 3 (elementos > 0):", novaLista3)
print("Nova Lista Combinada (cadrado de cada elemento * 2):", novaListaCombinada)
print ("Nova Lista 4 usando lambda: ", novaLista4)


#Se temos estas duas listas e queremos facer unha combinacion delas
l = [0,1,2,3]
m = ['a', 'b', 'c']

n = [r*s for s in l
     for r in m
     if s > 0 ]
print(n) # ['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc']
#Outra manera de facelo seria
p = []
for s in l:
    for r in m:
        if s > 0:
            p.append(s*r)
print(p) # ['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc']
# Facendoo coa funcion lambda
q = [(lambda r,s : r*s)(r,s)
     for s in l
     for r in m
     if s > 0 ]
print(q) # ['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc']
















