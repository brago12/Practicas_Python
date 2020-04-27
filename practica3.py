#PRACTICA3

#Hacer lo mismo que en la práctica 2 pero usando un bucle For en vez de While. Ojo, en vez de usar un For 
#con listas o tuplas, como explican en el curso que estáis haciendo, lo más sencillo es crear una progresión como 
#las que explican aquí





#Escribes palabras 
print ("Bienvenido a emparejando.com")
print ("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal.")
#Escribes y guardas la variable con la pregunta
varNombre = input("Tu nombre: ")
varNaci = int(input("Cuantos años tienes: "))

#INICIO DE BUCLE (Aquí contador está definido a 1)
for contador in range(varNaci): #Aquí comparamos para ver si es menor el contador con varNaci (Valgan lo que valgan)
	print ("Que no cumple " + str(contador))
#FIN DE BUCLE (Aquí contador ha cambiado y a partir de ahora tendrá otro valor)
print ("¡Qué sí cumple " + str(varNaci) + "!")

#Escribes palabras juntando variables
print ("Hola " + varNombre + ".Si no me equivoco, tienes " + str(varNaci) + " años ")

varWhile = True
#INICIO DEL BUCLE 
#Si varWhile es False,no hace ningun bucle y se queda con la respuesta proporcionada
while (varWhile==True):

	varTabu = input("¿Te gusta Taburete? ")

	if varTabu == "Si" or varTabu == "si" or varTabu == "SI":
	  print("OK Boomer, lo tuyo va a ser un caso difícil\n ")
	  varWhile = False
	elif varTabu == "No" or varTabu =="no" or varTabu =="NO":
	  print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.\n ")
	  varWhile = False
	else:
	  print ("Contesta con \"Si\" o \"No\"\n ")
	  #Si varWhile es igual a True, vuelve hacie el var
	  varWhile = True
#FIN DE BUCLE
#FIN DEL PROGRAMA