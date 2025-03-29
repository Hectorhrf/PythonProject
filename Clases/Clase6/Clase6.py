# Alt + Shift + E
#Ejercicio 1 mostrar los dias de las semana y mostrar el primero y el ultimo

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado",  "Domingo"]
print("El primer dia de la semana es el: ", dias[0])
print("El ultimo dia de la semana es el: ", dias[-1])
print("-------------------")


#Ejercicio 2 Modificar un elemento de una lista de frutas y añadir una al final

frutas = ["Manzana", "Platano", "Pera"]
frutas[0]="Mango"
print(frutas)
#Añadir
frutas.append("Sandia")
print(frutas)
print("-------------------")


#Ejercicio 3 crea una lista y añade tres colores

colores = []
print(colores)
colores.append("Rojo")
colores.append("Amarillo")
colores.append("Rojo")
print(colores)
print("-------------------")


#Ejercicio 4 ordena una lista y muestrala alreves

numeros = [9,13,8,5,7,4,2]
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
print("-------------------")


#Ejercicio 5 Elimina un elemento de una lista y muestra el resultado

animales = ["Perro", "Pulpo", "Gato", "Rinoceronte"]
print(animales)
animales.remove("Gato")
print(animales)
print("-------------------")


#Ejercicio 6 Contar cuantas veces aparece un elemento en la lista

numeritos = [4,6,7,8,2,3,4,5,6,7,8,9]
cantidad = numeritos.count(4)
print("Nº de veces que se repite el 4 es: ", cantidad)
print("-------------------")


#Ejercicio 7  crea una tupla con tres elementos de distinto tipo

mi_tupla = (19, "Hector", True)
print("Numero: ", mi_tupla[0])
print("String: ", mi_tupla[1])
print("Booleano: ", mi_tupla[2])
print("-------------------")


#Ejercicio 8 acceder al segundo elemento de una tupla anidada dentro de una lista1

datos = ["Nombre", (100,200), "apellido"]
tupla_intermedia = datos[1]
print(tupla_intermedia)
print("-------------------")


#Ejercicio 9 desempaquetar una tupla y mostrarlas

persona = ("Hector", 19, "Madrid")
nombre, edad, ciudad = persona
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Ciudad: ", ciudad)
print("-------------------")
