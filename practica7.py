#practica7
#Modifica el programa de la práctica 6 metiendo el código de cifrado dentro de una función 
#llamada cifracesar(texto,key) que devuelve el texto cifrado.

# Obtenemos mensaje a cifrar desde el usuario
# llamamos a upper para obtener sólo mayúsculas
texto = input("Mensaje: ").upper()

# Pedimos al usuario la cantidad de desplazamiento
num = int(input("Desplazamiento: "))

# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" + "abcdefghijklmnñopqrstuvwxyz"

# Variable para guardar mensaje cifrado

def cifracesar (texto,num) :
	cifrado = ""
	# Volvemos a hacer lo mismo por cada letra del mensaje
	for letra in texto: 
	    # Si la letra está en el abecedario se reemplaza
	    if letra in abc:
	        pos_letra = abc.index(letra)
	        # Sumamos para movernos a la derecha del abc
	        nueva_pos = (pos_letra + num) % len(abc)
	        cifrado+= abc[nueva_pos]
	    else:
	        # Si no está en el abecedario sólo añadelo
	        cifrado+= letra
	return cifrado

resultado = cifracesar(texto,num)
print("Mensaje cifrado:", resultado)
