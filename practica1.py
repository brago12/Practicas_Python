#PRACTICA1

# Escribe un programa que muestre el siguiente texto:

# BIENVENIDO A EMPAREJANDO.COM

# Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal.

# A continuación, el programa irá realizando algunas preguntas de una en una y guardando las respuestas en variables:

# Tu nombre: 
# Año de nacimiento: 
# ¿Te gusta Taburete?

# Y al final, responderá de la siguiente manera:

# Hola, “nombre”. Si no me equivoco, tienes “edad” años.

# Si le gusta taburete, dirá:

# OK Boomer, lo tuyo va a ser un caso difícil.

# Si no le gusta, dirá:

# Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.

#wasd







#Escribes palabras 
print ("Bienvenido a emparejando.com")
print ("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal.")
#Escribes y guardas la variable con la pregunta
varNombre = input("Tu nombre: ")
varNaci = int(input("Cuantos años tienes: "))

#Escribes palabras juntando variables
print ("Hola " + varNombre + ".Si no me equivoco, tienes " + str(varNaci) + " años ")

varWhile = True
#INICIO DEL BUCLE 
#Si varWhile es False,no hace ningun bucle y se queda con la respuesta proporcionada 

while varWhile:

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














 



