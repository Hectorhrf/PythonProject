#Ejercicio 1 Diccionario
#Crea un diccionario que almacene información de una persona: nombre,
#edad y si está registrado (booleano).

persona = {
    "nombre" : "Hector",
    "edad" : 19,
    "registradoEnElCenso" : True
}
print(persona)

#Ejercicio 2
#Imprime el valor de la clave "edad" del diccionario persona.

print(persona["edad"])

#Ejercicio 3
#Añade al diccionario persona la clave "ciudad" con valor "Madrid".

persona["ciudad"] = "Madrid"
print(persona)

#Ejercicio 4
#Cambia la edad de la persona a 31.

persona["edad"] = 20
print(persona)

#Ejercicio 5
#Elimina la clave "ciudad" del diccionario persona.

del persona["ciudad"]
print(persona)

#Ejercicio 6
#Crea una variable booleana que indique si existe la clave "nombre" en el diccionario persona.

exsiste_nombre = "nombre" and "patata" in persona
print(exsiste_nombre)

#Ejercicio 7
#Compara si la persona está registrada y tiene más de 18 años.
#Guarda el resultado en una variable booleana.

es_mayor_y_registrado = persona["edad"]>18 and persona["registradoEnElCenso"]
print(es_mayor_y_registrado)

#Ejercicio 8
#Invierte el valor de "registrado" y muestra el resultado.

no_registrado = not persona["registradoEnElCenso"]
print(no_registrado)

#Ejercicio 9
#Elimina duplicados de esta lista: [1, 2, 2, 3, 3, 3] usando un conjunto.

numeros = [1,2,2,3,4,5,3,4,5,2,1]
conjunto = set(numeros)
print(conjunto)

#ejercicio 10
#Compara si las listas [1, 2, 2, 3] y [3, 1, 2] tienen los mismos elementos únicos.

lista_a=set([1,2,3,4])
lista_b=set([4,3,2,1,5])

mismos_elementos = lista_a==lista_b
print(mismos_elementos)