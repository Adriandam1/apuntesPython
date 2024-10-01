

#Diccionario seria tambien una estructura de datos

#Contructor diccionario
outroDiccionario = dict()
#Estilo array:
#diccionario = {"Nombre":"Adrian"} Si printeamos nombre saldria Adiran
#Ejemplo manuel:
diccionario = { 2.0 : 2,
                "Dous" : 2,
                3.0 : 3,
                "Catro" : 4,
                5 : 5,
                'V': 5}

print (diccionario[2.0]) #Deberia devolver 2
print (diccionario['V']) #Deberia devolver 5
#Outra manera de facelo seria esta:
print(diccionario.get(2.0))
#get me permite poner un valor por defecto, en el caso de que no este en la coleccion
print(diccionario.get(6.0,"Non existe a clave"))
#tambien hay un metodo que me da o contido
print (diccionario.items()) #mostrase unha lista con duplas onde esta a clave e o valor do diccionario
#Tamen temos el keys que me da unha lista de claves
print (diccionario.keys())
#Tamen poderiamos obter a lista de valores solo
print (diccionario.values())
#E podo borrar, nun momento dado, un elemento
print (diccionario.pop(2.0, "Non existe a clave")) #borramos a clave 2.0 e poñemos un valor por defecto se se busca dita clave

print (diccionario.get(2.0))

#Se pueden hacer asignaciones
diccionario['V'] = "Cinco" #Cambiamos el valor de V a "cinco"
print(diccionario['V'])
























