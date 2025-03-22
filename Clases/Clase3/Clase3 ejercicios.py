#Ejercicio 1 Generador de nombres de usuario:
#Pide al usuario su nombre y apellido.
#Genera un nombre de usuario en minúsculas, sin espacios.
#Añade un número aleatorio al final.
#Muestra el nombre de usuario generado.

import random

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
nombre_usuario = (nombre + apellido).lower()
numero = random.randint(0, 99)
usuario_final = f"{nombre_usuario}{numero}"

print(f"Tu nombre de usuario es: {usuario_final}")


#Ejercicio 2 Analizador de clases:
#Pide al usuario que ingrese una frase.
#Muestra la cantidad de caracteres de la frase.
#Indica si la frase contiene la palabra "Python".
#Convierte la frase a mayúsculas.
#Muestra la frase invertida.

frase = input("Escribe una frase:")

print("Longitud de la frase:", len(frase))
print("¿Contiene 'Python'?:", "Python" in frase)
print("Frase en mayúsculas:", frase.upper())
print("Frase invertida:", frase[::-1])


#Ejercicio 3 Calculo de descuentos:
#Pide al usuario el precio de un producto.
#Aplica un 15% de descuento.
#Muestra el precio final con dos decimales.
#Muestra el precio redondeado hacia arriba.




#Ejercicio 4 Generador de etiquetas de productos:
#Pide el nombre de un producto y su precio.
#Convierte el nombre del producto a mayúsculas.
#Muestra el precio con dos decimales.
#Genera un código basado en el valor ASCII de la primera letra del producto.




#Ejercicio 5 Conversión de tipos y manipulación de listas:
#Pide al usuario una lista de números separados por comas.
#Convierte cada número a entero.
#Elimina los números repetidos.
#Muestra la lista ordenada sin duplicados.




#Ejercicio 6 Creación de mensajes personalizados:
#Pide al usuario su nombre, edad y ciudad.
#Muestra un mensaje con toda la información.
#Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad.




#Ejercicio 7 Generador de contraseñas aleatorias:
#Pide al usuario su nombre.
#Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
#Muestra la contraseña generada.




#Ejercicio 8 Verificacion de nombres en listas:
#Pide al usuario su nombre.
#Verifica si su nombre está en una lista de invitados predefinida.
#Si está en la lista, muestra su posición.




#Ejercicio 9 Manipulacion de nombres:
#Pide al usuario su nombre y apellido.
#Convierte el nombre a minúsculas y el apellido a mayúsculas.
#Genera un alias combinando las primeras 3 letras del nombre y del apellido.
#Muestra el alias generado.




#Ejercicio 10 Formatear y mostrar datos matemáticos:
#Pide al usuario un número decimal.
#Muestra el número redondeado a dos decimales.
#Calcula y muestra su cuadrado.
#Calcula y muestra su raíz cuadrada.

