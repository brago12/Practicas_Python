#PRACTICA6
#Programa tu primer cifrador César. El programa debe pedir al usuario una frase de texto en claro 
#y un número para cifrar. A continuación devolverá el texto cifrado.

#Mejora: convierte todo el texto en minúsculas antes de cifrarlo.





# Obtenemos mensaje a cifrar desde el usuario
# llamamos a upper para obtener sólo mayúsculas
texto = input("Mensaje: ").upper()

# Pedimos al usuario la cantidad de desplazamiento
n = int(input("Desplazamiento: "))

# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" + "abcdefghijklmnñopqrstuvwxyz"

# Variable para guardar mensaje cifrado
cifrado = ""

# Volvemos a hacer lo mismo por cada letra del mensaje
for letra in texto:
    # Si la letra está en el abecedario se reemplaza
    if letra in abc:
        pos_letra = abc.index(letra)
        # Sumamos para movernos a la derecha del abc
        nueva_pos = (pos_letra + n) % len(abc)
        cifrado+= abc[nueva_pos]
    else:
        # Si no está en el abecedario sólo añadelo
        cifrado+= letra

print("Mensaje cifrado:", cifrado)

