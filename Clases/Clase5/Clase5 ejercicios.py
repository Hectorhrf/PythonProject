#Ejercicio 1
#Evaluación de Expresiones Booleanas

expresion1 = 10>5
expresion2 = 7+3 ==10
expresion3 = 20<15
expresion4 = 4*2==9
print(expresion1, expresion2, expresion3, expresion4)

#Ejercicio 2
#Operaciones matemáticas con booleanos

print(True+True)
print(False+True)
print(False+False)
print(True*10)
print("MONEY "*10)
print(True*50)

#Ejercicio 3
#Conversión entre tipos básicos

print(int(True))
print(int(False))

#Ejercicio 4
#Propiedades de las cadenas

nombre = "Hector"

print(nombre[-1])
print(nombre[-2])
print(nombre[-3])
print(nombre[-4])
print(nombre[-5])
print (nombre[-6])


#Ejercicio 5
#Operaciones con cadenas y números

edad = 19
mensaje = "Tengo " + str(edad) + " años."
print(mensaje)

repetido = "Hola " * 3
print(repetido)

#Ejercicio 6
#Operaciones con caracteres y códigos ASCII

codigo = ord('A')
print(codigo)

letra = chr(66)
print(letra)

#Ejercicio 7
#Evaluación de expresiones lógicas

print(10 > 5 and 3 < 8)
print(5 == 5 or 2 > 10)
print(not (4 == 4 and 3 > 1))

#EJERCICIOS PARA CASA

#Ejercicio 1
#Comparación de números y booleanos
a = 14
b = 29
c = 47

mayor = a > b
menor = c < b
igual = a == c
diferente = b != c

print(mayor, menor, igual, diferente)

#Ejercicio 2
#Propiedades y manipulación de cadenas

frase = "Estoy usando python"
print(len(frase))
print(frase.upper())
print(frase.lower())
print(frase.count("o"))


#Ejercicio 3
#Operaciones matemáticas con números y booleanos

verdadero = True
falso = False
suma = verdadero + falso
resta = verdadero - falso
multiplicacion = verdadero * 2
multiplicacion_falsa = falso * 2
print(suma, resta, multiplicacion, multiplicacion_falsa)

#Ejercicio 4
#Extracción de caracteres en una cadena
cadena = "Modulo profesional optativo"
print(cadena[:3])
print(cadena[-3:])
print(cadena[::3])

#Ejercicio 5
#Conversión de tipos y evaluación booleana
num = 49
num_cadena = str(num)
print(num_cadena, type(num_cadena))

cadena_num = "10"
num_convertido = int(cadena_num)
print(num_convertido, type(num_convertido))
print(bool(""))
print(bool("Texto"))
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(None))
