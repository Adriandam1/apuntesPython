# Nome do arquivo: exemploDecoradores.py

# temos unha funcion e queremos decoara, añadirlle novas funcionalidades as que xa ten...
#quero engadirlle cosas a funcion
def funcion_necesita_decorador():
    print("Decorame, por favor!")

# creo unha funcion decoradora que recibe como parametro unha funcion a decorar
def meu_decorador(funcion_a_decorar):
#cando faga referencia o meu_decorador, podereia facer a funcion_necesita_decorador, con operacions previas e posteriores
    def funcion_envolvente():
        print ("Operacións antes da función a decorar")
        funcion_a_decorar()
        print("Operacións posteriores a execución da función a decorar")
    return funcion_envolvente

def meu_decorador2(funcion_a_decorar):
#cando faga referencia o meu_decorador, podereia facer a funcion_necesita_decorador, con operacions previas e posteriores
    def funcion_envolvente():
        print ("Outras operacións antes da función a decorar")
        funcion_a_decorar()
        print("Outras operacións posteriores a execución da función a decorar")
    return funcion_envolvente

#Executariamos da seguinte maneira:
funcion_decorada = meu_decorador(funcion_necesita_decorador)
funcion_decorada()

print("\n") # espacio en blanco para no mezclar las llamadas

#Outra manera de facelo:

#Neste caso estou dicindolle a funcion2 que lle aplice meu_decorador
@meu_decorador2
@meu_decorador
def funcion2_necesita_decorador():
    print ("Eu tamén preciso que me decoren!")

funcion2_necesita_decorador()
# Comprobamos con multiples decoradores como a funcion e envolta nos decoradores


























