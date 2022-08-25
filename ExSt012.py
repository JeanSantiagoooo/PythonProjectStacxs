"""
Escreva um programa para ler 3 valores inteiros
(considere que não serão lidos valores iguais)
e escrevê-los em ordem crescente.
"""
Valor1 = int(input("Digite o PRIMEIRO valor: "))
Valor2 = int(input("Digite o SEGUNDO valor: "))
Valor3 = int(input("Digite o TERCEIRO valor: "))

if Valor1 == Valor2 or Valor2 == Valor3:
    print("Digite apenas numero diferentes. ")

elif Valor1 < Valor2 and Valor2 < Valor3:
    print(Valor1, Valor2, Valor3)

elif Valor1 < Valor3 and Valor3 < Valor2:
    print(Valor1, Valor3, Valor2)

elif Valor2 < Valor1 and Valor1 < Valor3:
    print(Valor2, Valor1, Valor3)

elif Valor2 < Valor3 and Valor3 < Valor1:
    print(Valor2, Valor3, Valor1)

elif Valor3 < Valor1 and Valor1 < Valor2:
    print(Valor3, Valor1, Valor2)

elif Valor3 < Valor2 and Valor2 < Valor1:
    print(Valor3, Valor2, Valor1)
