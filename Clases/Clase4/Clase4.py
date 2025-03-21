# Ejercicio 1: Operaciones numericas complejas.
# Define cinco variables numericas distintas (int, float, complex).
# realiza diversas operaciones matematicas (potencias, division entera, modulo).
# Imprime los resultados en una cadena clara y descriptiva.

num1 = 5
num2, num3, num4, num5 = 10,3,8.7,4+2j
resultado= (f"\nPotencia: {num1 ** num2}, "
            f"\nDivision entera: {num1 // num2}, "
            f"\nModulo: {num1 % num2}, "
            f"\nMultiplicacion: {num3 * num4}, "
            f"\nComplejo: {num5}"
           )
print(resultado) # "\n" para hacer saltos de linea

#Ejercicio 2: Combinacion de cadenas y numeros

num_int, num_float = 8, 3.5
cadena1, cadena2, cadena3 = "Resultado: ","La suma es: ", "y la division es: "
resultado = cadena1 + " " +  cadena2 + " " + str(num_int+num_float) + " " + cadena3 + " " + str(num_int/num_float)

print(resultado)

#Ejercicio 3: Manipulacion avanzada de cadenas

cadena = " Esto es un ejemplo con huecos delante y detras "
nueva_cadena = cadena.strip().upper().split()
print(nueva_cadena)

#Ejercicio 4: Indices y subcadenas
cadena_extensa = "Python es un lenguaje que me encanta y me da mucho trabajo"
subcadena= (cadena_extensa[0:6]+ "" +
            cadena_extensa[11:20] + "" +
            cadena_extensa[-9:])
resultado2 = subcadena[::-1]
print(resultado2)

#Ejercicio 5: Formato y conversion numerica

entero, flotante, complejo = 12, 367.7864574, 5+3j
formato = (f"Entero: {entero}, Flotante: {flotante:.2f}, "
           f"Notacion cientifica: {flotante:.2e} , Complejo: {complejo}, "
           )
print(formato)