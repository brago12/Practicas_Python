#PRACTICA5
#Repite la Práctica 4 pero guardando los datos del usuario en una variable de tipo diccionario en lugar de en una lista.
varNombre = input("Tu nombre: ")
varNaci = int(input("Cuantos años tienes: "))
dicci = {"Edad" : varNaci , "Nombre" : varNombre}
for elemento in dicci:
	print ("Elemento : " + str(dicci[elemento]))



#Listas:
	#CREARLA: lista=[variable,"pepito", 13, ...]
	#"pepito": lista[1]
	#Posicion "pepito": lista.index("pepito")
	#longitud(tamaño) : len(lista)
#Diccionarios:
	#CREARLO: diccionario={"calle" : variable,"nombre" : "pepito", "edad" : 13, ...}
	#"pepito": diccionario["nombre"]
	#keys : datos_basicos.keys()) 
	#values : datos_basicos.values()
	#items : datos_basicos.items()
	#longitud(tamaño) : len(diccionario)
#for clave, valor in diccionario.iteritems(): 
#print "El valor de la clave %s es %s" % (clave, valor)
#print("El valor de la clave "+str(clave)+" es "+str(valor))

#La verdad tras un diccionario:
	#En los demás lenguajes un diccionario se llama Objecto
	#El objeto siempre se hace con llaves: varObject = {}
	#El objeto siempre tiene claves: varObject = {
	# "nombre": "Juan"
	# "apellido": "Retana"
	#}
	#En otros lenguajes para acceder a "Juan" es con varObject.nombre