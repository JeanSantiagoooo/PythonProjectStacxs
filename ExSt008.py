"""
Escreva um programa para ler 2 valores (considere que não serão informados valores iguais)
e escrever o maior deles.
"""

while True:
    Valor1 = int(input("Digite um número: "))
    Valor2 = int(input("Digite um número: "))
    if Valor1 > Valor2:
        print(("O maior valor é o primeiro: "), Valor1)

    else:
        print(("O maior valor é o segundo: "), Valor2)
