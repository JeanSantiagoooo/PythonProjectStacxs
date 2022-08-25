"""
Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
 Considere que o usuário não informará valores iguais.
"""

Valor1 = int(input("Digite o PRIMEIRO valor: "))
Valor2 = int(input("Digite o SEGUNDO valor: "))
Valor3 = int(input("Digite o TERCEIRO valor: "))

if Valor1 == Valor2 or Valor2 == Valor3:
    print("Digite apenas numero diferentes. ")

elif Valor1 > Valor2 and Valor1 > Valor3:
    print("O maior valor é: ", Valor1)

elif Valor2 > Valor1 and Valor2 > Valor3:
    print("O maior valor é: ", Valor2)

else:
    print("O maior valor é: ", Valor3)
