#Una lista seria un "array superflexible (no es una array es una coleccion de objetos)

#Ejemplos de listas

lista = [2, 3.0, "Cadeas", [2,1,4], (2,3)]
# muestras el elemento en la posicion 3
print (lista[3])

#muestra los elementos de la lista a partir del elementos 2 incluido
print (lista[2::])

#muestra el primer elemnto y la lista hasta el cuarto elemento
print (lista [0:4])

#muestra el segundo elemento, el cuarto(da un salto de 2 elementos)
print (lista[1::2])

#Cambia el elemento 2 que hasta aqui es "3.0" pasara a "Texto"
lista [2] = "Texto"
print (lista)

#Cambia el elemento tercero que es un array el elemento en posicion 1 por "tres"
lista [3][1] = "Tres"
print (lista)

#Cambia los elementos que estan a partir del elemento 1 al elemento 3 por lo sque ponemos, luego continua con la lista
lista [1:3] = ["Tres punto cero", "Secuencia de caracteres", "Outros", "Ele", "Mentos"]
print (lista)

#La dupla no puede ser modificada partcialmente, no puedes cambair un elemento, para modificarla debe cambiarse completamente



