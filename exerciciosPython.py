# !/usr/bin/env python

# TODO COMENTADO CON COMILLAS PARA EVITAR PROBLEMAS EJECUCION

""" Un programa sinxelo, para calcular cadrados
de números

def num_cadrados (num):
    print ("O cadrado de " +str(num) + " é: " +str (num*num))



def potencia():
    print("Calcularanse potencia de dous números")
    n1 = input("Ingrese un número enteiro: ")
    n2 = input("Ingrese otro número enteiro: ")

    for x in range(int(n1), int(n2)):
        #print("O valor de x é: " +str(x))
        #print(x * x)
        num_cadrados(x)

    #print("O valor de x fora do ciclo e: " +str(x))
    print("É todo por agora")

#exercicio 1.8 - 3
def factorial(n):

    factorial = 0

    for i in range (1,n+1) :
        factorial = factorial*i

    return factorial

potencia()
n = input("Ingrese un número enteiro para facer o factorial: ")
print (factorial (int(n)))

# exercicio 7.2

def fichasDominoEncaixan (cadeaFichas):
    #As fichas teñen un formato: (2-3) (4-5)
    fichas = cadeaFichas.split(' ')
    #print (fichas)
    novaLista = list()
    for ficha in fichas:
        novaLista.append(ficha.split('-'))
    #print (novaLista)
    encaixan = False
    if novaLista[0][0] == novaLista[1][0]:
        encaixan = True
    elif novaLista[0][0] == novaLista[1][1]:
        encaixan = True
    elif novaLista[0][1] == novaLista[1][0]:
        encaixan = True
    elif novaLista[0][1] == novaLista[1][1]:
        encaixan = True
    return encaixan


print (fichasDominoEncaixan('2-3 4-5')) # se printea: ['2-3', '4-5']
#Temos feito unha lista con dous elementos
#Poderiamos convertir esto en novaLista = [[2,3].[4.5]]


# exercicio 7.2 Manera de hacerlo B

def fichasDominoEncaixanB (cadeaFichas):
    #As fichas teñen un formato: (2-3) (4-5)
    fichas = cadeaFichas.split(' ')

    for i, ficha in enumerate(fichas):
        fichas[i] = ficha.split('-')
    encaixan = False
    if fichas[0][0] == fichas[1][0]:
        encaixan = True
    elif fichas[0][0] == fichas[1][1]:
        encaixan = True
    elif fichas[0][1] == fichas[1][0]:
        encaixan = True
    elif fichas[0][1] == fichas[1][1]:
        encaixan = True
    return encaixan
print (fichasDominoEncaixanB('2-3 4-5'))

# exercicio 7.2 Manera de hacerlo C
# el que le gusta a Manuel por algun motivo
def fichasDominoEncaixanC (cadeaFichas):
    #As fichas teñen un formato: (2-3) (4-5)
    fichas = cadeaFichas.split(' ')

    encaixan = False
    if fichas[0][0] == fichas[1][0]:
        encaixan = True
    elif fichas[0][0] == fichas[1][2]:
        encaixan = True
    elif fichas[0][2] == fichas[1][0]:
        encaixan = True
    elif fichas[0][2] == fichas[1][2]:
        encaixan = True
    return encaixan

print (fichasDominoEncaixanC('2-3 3-5'))
print (fichasDominoEncaixanC('2-3 4-5'))
print (fichasDominoEncaixanC('4-5 5-6'))

"""
from sentenciasCondicionais import elemento

### EXERCICIO 7.5 Dada unha lista de números enteiros, escribir unha función que:

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# a) Devolte unha lista con tódolos que sexan primos.
def nPrimo(n):
    primo = True
    if n !=0 and n !=1:
        for num in range (1,n):
            if n % num == 0:
                primo = False
                break
    return primo
primos = [n for n in lista if nPrimo(n)]
print(primos)
# b) Devolte a sumatoria e o promedio dos valores.

# c) Devuelva unha lista co factorial de cada un desos números.






















