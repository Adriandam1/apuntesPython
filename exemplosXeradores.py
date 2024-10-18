# Nome do arquivo: exemplosXeradores.py

#Os xeradores seria algo parecido a xear valores instantaneos, non vale para tódo eh,
# nos nun momento dado podemos querer xerar un valor de usar y tirar, que xenero nun momento dado e logo podo descartalo

#A maneira de crear un xerador e parecida o exemplo que vimos nas listas:
'''
lista = [-2,-1,0, 1,2,3,4,5,6,7,8,9]

novaLista =[num*2 for num in lista]
novaLista2 =[cadrado (n) for n in lista]
novaLista3 = [n for n in lista if n>0]
novaListaCombinada = [cadrado(num * 2) for num in lista]
novaLista4 = [(lambda n : n**2)(n) for n in lista]
'''
#Exemplo:
l = [-2,-1,0, 1,2,3,4,5,6,7,8,9]
x = (n**2 for n in l)
print (x) # resultado: <generator object <genexpr> at 0x7f45a5519630>

#para acceder a eso que xenera o teño que facer cun for
# cando eu itero no xerador el vai xerando os datos no momento,
# o de arriba e unha funcion
for n in x:
    print(n)

# como cosa curiosa para que o vexades, seria unha funcion especial
# si quixeramos facelo de esta maneira, fixadevos:
# este de aqui faria o mesmo que o anterior:
def meu_xerador (l):
    for n in l:
        yield n**2

for n in meu_xerador(l):
    #print("meu_xerador di " + str(n))
    print (meu_xerador.__name__+" di "+str(n))

'''
lista = list()
for elemento in x:
    lista.append(elemento)
tupla = tuple (meu_xerador(l))
print(lista)
print(tupla)
'''















