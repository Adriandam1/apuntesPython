# if
#si declaramos un if la condicion no va a tener
#la sentencia if se cierra con 2 puntos :
#el if se respeta la linea, mientras este dentro del mismo nivel sigues dentro del if, aunque la diferencia solo sea un especio, sales y entras del if
#importantisimo el sangrado del if clave
variable = 3
if variable == 5 :
    print ("A variable é: "+str(variable)) #no podemos meter int dentro de string, tenemos que hacer un cast
    print ("Dentro deo if")
elif variable == 3:
    print ("A variable é: "+str(variable)) # siempre respetando las sangrias
else:
    print("A variable non é 5") # el else tambien funciona con la sangrias CUIDADO
if variable == 3 :
    print ("A variable é: "+str(variable))
    print ("Dentro doutro if")

print ("Fora do if, non depende da condicion")

#Os lembrais do seguinte en java? Operador ternario java:
# String variable = (num%2==0)? "par" : "impar"
#En python equivalente a esto
par = True if variable%2==0 else False

#Otra manera de escribirlo seria:
if variable%2==0:
    par = True
else:
    par = False

#Como facemos un while?
#Neste caso como a variable e 3 se executa 3 veces( 4, 5 y 6)
while variable < 6:
    variable = variable + 1
    print ("Variable é: "+ str(variable))

# Como se fqi o bucle do while en Python? Non existe como tal
# Xa ahi temos que xogar con... esta seria a unica manera de facer un do while

#bucle infinito:
i = 0
while True:
    #aqui verian as instrucciones
    print("Instrucciones a facer polo menos unha vez, neste caso a: " + str(i+1) +"ª")
    i = i + 1
    # bucle de salida
    if i < 5:
        continue
    else:
        break
#Conclusion... NO HAY DO WHILE


#contruimos unha lista e reutilizamos o anterior por comodidad
i = 0
lista =['Un', 'Dous', 'Tres', "Catro", 'V']
while True:
    #aqui verian as instrucciones
    print("Instrucciones a facer polo menos unha vez, neste caso a: " + str(i+1) +"ª")
    print (lista [i])
    i = i + 1
    # bucle de salida
    #Funcion len que nos indica a lonxitude da lista (nexte caso 5)
    if i < len(lista):
        continue
    else:
        break
#Continuamos con el bucle for, que no es for, es "for in" (usamos a lista anteeior)
#En java: for (i = 0, i < 5, i++){ bloque de codigo}
# "numero" e un nome de variable, estamos xerando unha nova variable
# Esto nos permite listar unha lista completa e a mellor opcion, e a que debes utilizar
for numero in lista:
    print ("O elemento en lista è: "+ numero)

# a continuacion usamos o for i
#Creamos variable para sacar a lonxitude da lista
lonxitudeLista = len (lista)
#Temos que crear o indice, o xerador "range" vai xenerar unha secuencia de numeros como queiramos
#incidamos o inicio se non lle damos valor a range por defecto xa e 0
#traducido: for i in range(inicio, final, incremento)
for i in range(0, lonxitudeLista, 1):
#Funcionaria igual porque e o por defecto: for i in range(lonxitudeLista);
    print ("i e: " +str(i))
    print (lista [i])

diccionario = { 2.0 : 2, "Dous" : 2, 3.0 : 3, "Catro" : 4, 5 : 5, 'V': 5}
for elemento in diccionario:
    print (elemento)

#Outra funcion intersante e "enumerate"
#A funciona enumerate recorre a lista
for indice, elemento in enumerate(lista):
    print ("O indice é: "+ str(indice))
    print ("O elemento é: "+ elemento)


























