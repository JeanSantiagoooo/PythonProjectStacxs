"""
Escreva um programa que leia as medidas dos lados de um triângulo e escreva
 se ele é Equilátero, Isósceles ou Escaleno.

Sendo que:

Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isóscele: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.
"""

Lado1 = float(input("Digite o valor do lado 1: "))
Lado2 = float(input("Digite o valor do lado 2: "))
Lado3 = float(input("Digite o valor do lado 3: "))

if Lado1 == Lado2 and Lado1 == Lado3:
    print("Trata-se de um Triângulo Equilátero")
elif Lado1 == Lado2 and Lado2 != Lado3:
    print("Trata-se de um Triângulo Isóscele")
elif Lado1 != Lado2 and Lado1 == Lado3:
    print("Trata-se de um Triângulo Isóscele")
elif Lado1 != Lado2 and Lado2 == Lado3:
    print("Trata-se de um Triângulo Isóscele")
else:
    print("Trata-se de um Triângulo Escaleno")

