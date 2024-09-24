# !/usr/bin/env python
""" Un programa sinxelo, para calcular cadrados
de números """

def num_cadrados (num):
    print ("O cadrado de " +str(num) + " é: " +str (num*num))



def potencia():
    print("Calcularanse potencia de dous números")
    n1 = input("Ingrese un número enteiro: ")
    n2 = input("Ingrese otro número enteiro: ")

    for x in range(int(n1), int(n2)):
        print("O valor de x é: " +str(x))
        print(x * x)
        num_cadrados(x)

    print("O valor de x fora do ciclo e: " +str(x))
    print("É todo por agora")
potencia()


































