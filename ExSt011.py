"""
As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25
se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs
compradas, calcule e escreva o valor total da compra.
"""


Quantidade = int(input("Quantas maçãs foram compredas: "))

if Quantidade > 12:
    ValorPagar = Quantidade * 0.30
    print("O total a pagar é: $", ValorPagar,)

else:
    ValorPagar = Quantidade * 0.25
    print("O total a pagar é: $", ValorPagar, )