import math
import random

#1. len para mirar la longitud de una cadena o string
nombre = "Bruno"
print("Longitud del nombre: " , len(nombre))

#2. Upper y Lower para convertir en mayusculas y minusculas
print("Quiero tener mi nombre en mayusculas: ", nombre.upper())
print("quiero tener mi nombre en minusculas: ", nombre.lower())

# Dame los 3 primeros caracteres
print("Los primeros 3 caracteres de mi nombre: ", nombre[:3])
# Dame los 4 ultimos caracteres
print("Los ultimos 4 caracteres de mi nombre: ", nombre[:-4])

#4. Remplazar palabras en un String
frase = "Me encanta Java"
print("Quiero cambiar una palabra: ", frase.replace("java", "python"))
print("Impresion tras reemplazo de palabra: ", frase)

#5.Verificar si una cadena
print("Python" in frase) #False
nueva_frase = ["Me encanta Python"]
print("Python" in nueva_frase) #True

#6. Unir varias palabras en un solo string o cadena
palabras = ["Hola", "mundo", "Python"]
print("La frase completa es:", " ".join(palabras))

#7. Dividir una cadena en partes
oracion = "Python es la leche, el mejor, el capo de capos"
palabras = oracion.split()
print("Lista de palabras: ", palabras)

#8. Redondear un numero que sea decimal
numero = 3.1416
print("El numero PI redondeado es: ", round(numero/2))

#9. Formatear numeros con decimales
precio = 19.99
print("Precios con dos decimales: {:.2f}".format(precio))

#10. Obtener el valor ASCII de un caracter
print("Condigo ASCII de 'A': ", ord('A'))

#11. Elevar un numero al cuadrado
numerito = 5
print("5 elevado al cuadrado es: ", numerito **3)

#12. Obtener raiz cuadrada
print("Raiz cuadrada de 25 es: ", 25 ** 0.5)
#Alternativa importando sqrt con math. Piensa que tienes el import arriba del doc
numero_raiz=16
raiz_numero= math.sqrt(numero_raiz)

print(raiz_numero)
print("Raiz cuadrada del numero es : ", raiz_numero)

#13.Divisiones, restos y modulos
print("Division normal: ", 10/3)
print("Division entera: ", 10//3)
print("Resto: ", 10%3)

#14. Generar numeros aleatorios
print("Numero aleatorio del 1 al 10: ", random.randint(1,10))

#15. Convertir cadenas a numeros y viceversa
numero_a_cadena = 100
texto = str(numero_a_cadena)
print("Convertido a texto, queda: ", texto)

cadena_a_numero = "200"
numero_a_cadena = int(cadena_a_numero)
print  ("Convertir a entero, queda: ",cadena_a_numero)

#16. Redondear siempre hacia arriba
print("redondear hacia arriba del numero 3.2: ", math.ceil(3.2))
print("redondeo hacia abajo del numero 3.2: ", math.floor(3.2))

#17. Convertir una lista en un conjunto(eliminando duplicados)
numeros =[1,2,2,3,4,4,5]
sin_duplicados = set(numeros)
print("Lista sin duplicados: ", sin_duplicados)

#18. Absurdo PERo. Repetir una cadena varias veces
print("python!"*3)

#19. Obtener el tipo de una variable
dato = 9.98
print("tipo de dato: ", type(dato))

#20. Combinar cadenas y variables en un print
nombreprofe = "Mario"
edad = 32
print(f"Hola soy {nombreprofe} y tengo {edad} años")