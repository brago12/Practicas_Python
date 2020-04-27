#PRACTICA4
#Partiendo de la Práctica 2 o la 3, guardar la información 
#del usuario en una variable de tipo lista. A continuación, imprimir los datos de la lista usando un bucle For.

varNombre = input("Tu nombre: ")
varNaci = int(input("Cuantos años tienes: "))
lista = [varNaci , varNombre]
for elemento in lista:
	print ("Elemento " +str(lista.index(elemento))+ " : " + str(elemento))
