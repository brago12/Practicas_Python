#PRACTICA2

# Partiendo del programa anterior, añadir un bucle while que cuente desde el 1 hasta la edad del usuario y escriba en pantalla las siguientes frases:

# Que no cumple 1
# Que no cumple 2
# Que no cumple 3
# …
# ¡Qué sí cumple “años”!




#Escribes palabras 
print ("Bienvenido a emparejando.com")
print ("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal.")
#Escribes y guardas la variable con la pregunta
varNombre = input("Tu nombre: ")
varNaci = int(input("Cuantos años tienes: "))

contador = 1
#INICIO DE BUCLE (Aquí contador está definido a 1)
while (contador<varNaci): #Aquí comparamos para ver si es menor el contador con varNaci (Valgan lo que valgan)
	print ("Que no cumple " + str(contador))
	contador = contador + 1 #Aquí literalmente definimos contador a otro valor (incrementamos en 1)
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