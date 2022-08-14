#Tarefa IF4:

#Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a
#seguir, calcule e mostre o valor a receber. Sabe-se que este é composto pelo
#salário bruto acrescido de gratificação e descontado o imposto de 7% sobre o salário.

Gratificacao:float
Soma:float
SalarioBruto=(float(input("Digite o valor do salário bruto: ")))

if SalarioBruto <= 350.00:
    Gratificacao = 100.00
elif SalarioBruto > 350 and SalarioBruto <= 600:
    Gratificacao = 75.00
elif SalarioBruto > 600 and SalarioBruto <= 900:
    Gratificacao = 50.00
else:
    Gratificacao = 35.00

Soma = SalarioBruto + Gratificacao
ValorReceber = Soma - (Soma * 0.07)

print("O valor do salário, somado a gratificação menos impostos, é: R$ ", ValorReceber)


