# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella

print("Combinacion de Palabras \n")

print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados

acronimo=palabra_1[:3]+palabra_2[:2]

print("En Acronimo formado entre las dos palabras ingresadas es: ", acronimo)

print("Se utilizaron las 3 primeras letras de la primera palabra ingresada y las 2 primeras de la segunda palabra ingresada")

print("Fin del Programa")
