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

import math

precio = float(input("Precio del producto:"))
descuento = precio * 0.15
precio_final = precio - descuento
print(f"Precio con descuento: ${precio_final:.2f}")
print(f"Redondeado hacia arriba: ${math.ceil(precio_final)}")


#Ejercicio 4 Generador de etiquetas de productos:
#Pide el nombre de un producto y su precio.
#Convierte el nombre del producto a mayúsculas.
#Muestra el precio con dos decimales.
#Genera un código basado en el valor ASCII de la primera letra del producto.

producto = input("Nombre del producto")
precio = float(input("Precio del producto: "))
etiqueta = f"PRODUCTO: {producto.upper()} - PRECIO: ${precio:.2f} - CÓDIGO DEL PRODUCTO: {ord(producto[0])}"

print(etiqueta)

#Ejercicio 5 Conversión de tipos y manipulación de listas:
#Pide al usuario una lista de números separados por comas.
#Convierte cada número a entero.
#Elimina los números repetidos.
#Muestra la lista ordenada sin duplicados.

numeros = input("Escribe una lista de numeros separados por coma: ")
lista_numeros = list(set(map(int, numeros.split(","))))
print("Lista y ordenada y sin numeros duplicados:", sorted(lista_numeros))


#Ejercicio 6 Creación de mensajes personalizados:
#Pide al usuario su nombre, edad y ciudad.
#Muestra un mensaje con toda la información.

import math

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
ciudad = input("Escribe tu ciudad: ")
edad_redondeada = math.ceil(edad / 18) * 18
mensaje = f"Hola {nombre}, tienes {edad} años y vives en {ciudad}. Mayoria de edad: {edad_redondeada}."

print(mensaje)


#Ejercicio 7 Generador de contraseñas aleatorias:
#Pide al usuario su nombre.
#Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
#Muestra la contraseña generada.

import random

nombre = input("Escribe tu nombre: ")
contraseña_aleatoria = f"{nombre[0].upper()}-{random.randint(100, 999)}-*"

print(f"La contraseña es: {contraseña_aleatoria}")


#Ejercicio 8 Verificacion de nombres en listas:
#Pide al usuario su nombre.
#Verifica si su nombre está en una lista de invitados predefinida.
#Si está en la lista, muestra su posición.

invitados = ["Hector, Bruno, Andres, Jose"]
nombre = input("Escribe tu nombre: ")

if nombre in invitados:
    print(f"Bienvenido, {nombre}! Estás en la posición {invitados.index(nombre) + 1}.")
else:
    print("No estas en la lista")


#Ejercicio 9 Manipulacion de nombres:
#Pide al usuario su nombre y apellido.
#Convierte el nombre a minúsculas y el apellido a mayúsculas.
#Genera un alias combinando las primeras 3 letras del nombre y del apellido.
#Muestra el alias generado.

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
alias = nombre[:3].lower() + apellido[:3].upper()

print(f"Tu alias es: {alias}")


#Ejercicio 10 Formatear y mostrar datos matemáticos:
#Pide al usuario un número decimal.
#Muestra el número redondeado a dos decimales.
#Calcula y muestra su cuadrado.
#Calcula y muestra su raíz cuadrada.

numero = float(input("Escribe un número decimal: "))

print(f"Número redondeado: {round(numero, 2)}")
print(f"Cuadrado: {numero ** 2}")
print(f"Raíz cuadrada: {numero ** 0.5}")

