"""
Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva
se o triângulo é Acutângulo, Retângulo ou Obtusângulo.

Sendo que:

Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90º)
TriânguloAcutângulo: possui três ângulos agudos. (menor que 90º
"""

Ang1 = print("Digite o valor do primeiro angulo: ")
Ang2 = print("Digite o valor do segundo angulo: ")
Ang3 = print("Digite o valor do terceiro angulo: ")

if Ang1 == 90 or Ang2 == 90 or Ang3 == 90:
    print("A figura é um Triangulo Retangulo")
elif Ang1 > 90 or Ang2 > 90 or Ang3 > 90:
    print("A figura é um Triangulo Obtusângulo")
else:
    print("A figura é um Triangulo Acutângulo")