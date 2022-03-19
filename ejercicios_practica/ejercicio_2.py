# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
from __future__ import division
from email.mime import multipart


print('Ingrese por consola el primer número entero a operar (ejemplo 1,2,3,4,25,33,160):')
numero_1 = int(input())

print('Ingrese por consola el segundo número entero a operar (ejemplo 1,2,3,4,25,33,160):')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números enteros solicitados
# print(....)

print("El primer numero ingresado es: ", numero_1, "\n")

print("El segundo numero ingresado es: ", numero_2, "\n")


# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma

suma=numero_1+numero_2

print("El resultado de sumar el primer numero ingreado", numero_1, " y el segundo numero ingresado ", numero_2, " es ", suma)

# Resta

resta=numero_1-numero_2

print("El resultado de restar el primer numero ingreado", numero_1, " y el segundo numero ingresado ", numero_2, " es ", resta)

# División

division=numero_1//numero_2

print("El resultado de dividir el primer numero ingreado", numero_1, " por el segundo numero ingresado ", numero_2, " es ", division)


# Multiplicación

multiplicacion=numero_1*numero_2

print("El resultado de multiplicar el primer numero ingreado", numero_1, " por el segundo numero ingresado ", numero_2, " es ", multiplicacion)

print("Fin del Programa")
