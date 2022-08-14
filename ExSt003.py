#Tarefa IF3:
#O que

#Faça um programa que receba a idade de um nadador e mostre sua
#categoria, usando as regras a seguir.Para idade inferior a 5,
#qualmensagem deveríamos mostrar

Idade = int(input("Digite sua idade: "))

if Idade < 5:
    print("Não tem uma categoria para essa idade!")
elif Idade >= 5 and Idade <= 7:
    print("Sua categoria é: Infantil")
elif Idade >= 8 and Idade <= 10:
    print("Sua categoria é: Juvenil")
elif Idade >= 11 and Idade <= 15:
    print("Sua categoria é: Adolescente")
elif Idade >= 16 and Idade <= 30:
    print("Sua categoria é: Adulto")
else:
    print("Sua categoria é: Sênior")