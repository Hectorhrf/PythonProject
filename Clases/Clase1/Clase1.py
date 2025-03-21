#--Operaciones arigmeticas--

#numeros normales
numero_entero = 19
numero_negativo = -12
print("Soy un numero entero, en concreto, soy el ", numero_entero)
print("Soy un numero entero, en concreto, soy el 19")

#numeros decimales
numero_decimal = 3.14
numero_decimal_negativo = -10.5
print("soy un numero decimal:",numero_decimal)
print("soy un numero decimal:",numero_decimal_negativo)

#numeros complejos
num_complejo = 2 + 3j
print("soy un numero muy complejo",num_complejo)
print("Parte real",num_complejo.real)
print("Parte imaginaria",num_complejo.imag)
print("tipo de dato",type(num_complejo))

#operaciones
suma = 10 + 5
resta = 10 - 3
multiplicaicion =4*2
division = 10/3
division_entera = 10%3
potencia = 2**3

print("\nOperaciones matematicas")
print("Suma:", suma, "| Division:", division,"| Division entera: ",division_entera)

#--BOOLEANOS--

es_python_facil = True
es_python_dificil = False

print("booleanos")
print("\n¿Es Python fácil?:",es_python_facil)
print("¿Es Python dificil?:",es_python_dificil)

mayor_que = 10>5 #me devuelve true
menor_que = 10<5 #me devuelve false
igualdad = 10 == 10 #me devuelve true
diferente = 10 != 5 #me devuelve true