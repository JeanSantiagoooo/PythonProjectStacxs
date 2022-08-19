"""
Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem
que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que
ela nasceu).
"""



AnoAtual = 2022
AnoNascimento = int(input("Digite o ano do seu nascimento: "))
Idade = AnoAtual - AnoNascimento
print(Idade)
if Idade >= 18 and Idade < 70:
    print("Você Poderá votar esse ano.")

elif Idade >= 70 or Idade < 18 and Idade >= 16:
    print("Você poderá votar esse ano, se quiser.")

else:
    print("Você ainda não tem idade para votar")