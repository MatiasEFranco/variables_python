# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

num1=float(input("Por favor, ingrese el primer valor: "))
num2=float(input("Por favor, ingrese el segundo valor: "))
print('''Que operacion desea realizar?
 A) Suma
 B) Resta
 C) Multiplicación
 D) División
 E) Exponente/Potencia''')

operador=input("Ingrese la letra de la que corresponde a la operacion que desea realizar: ")

if operador.lower() == "a":
  
  print("La suma es ", num1+num2)

elif operador.lower() == "b":

    print("La resta es ", num1-num2)

elif operador.lower() == "c":

    print("La multiplicacion es ", num1*num2)

elif operador.lower() == "d":

    print("La division de ", num1, " sobre ", num2, " es ",  num1//num2)

elif operador.lower() == "e":

    print("La Potencia de ", num1, " elevado a ", num2, " es ", num1**num2 )

else :

  print("Error, no se ingreso una operacion valida")

print("Fin del Programa")
