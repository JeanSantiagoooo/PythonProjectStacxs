"""
Faça um programa que leia um conjunto não determinado de valores e mostre
o valor lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada
de dados com um valor negativo ou zero.

"""
import math

Quadrado = Cubo = Raiz = 0

while True:
    Numero = float(input("Digite um numero maior que zero: "))
    print(Numero)
    if Numero > 0:
        Quadrado = pow(Numero,2)
        print("O quadrado do número é: ", Quadrado)
        Cubo = pow(Numero,3)
        print("O cubo do número é: ", Cubo)
        Raiz = math.sqrt(Numero)
        print("A Raiz do número é: ", Raiz)
        continue
    else:
        print("Fim do programa")
        break

