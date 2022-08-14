# Algoritimo 001: Idade e Peso
# Dev: Jean Santiago
# Data: 12/08/2022

Idade = (int(input("Digite a idade: ")))
Peso = (float(input("Digite seu peso: ")))


if(Peso <= 60 and Idade < 20):
    print("Seu grupo de Risco é 9.")

elif(Peso >= 60 and Peso <= 90 and Idade < 20):
    print("Seu grupo de Risco é 8.")

elif(Peso > 90 and Idade < 20):
    print("Seu grupo de Risco é 7.")

elif(Peso <= 60 and Idade >= 20 and Idade <= 50):
    print("Seu grupo de Risco é 6.")

elif(Peso > 60 and Peso <= 90 and Idade >= 20 and Idade <= 50):
    print("Seu grupo de risco é 5")

elif(Peso > 90 and Idade >= 20 and Idade <= 50):
    print("Seu grupo de Risco é 4.")

elif(Peso <= 60 and Idade > 50):
    print("Seu grupo de Risco é 3.")

elif(Peso > 60 and Peso <= 90 and Idade > 50):
    print("Seu grupo de Risco é 2.")

elif(Peso > 90 and Idade > 50):
    print("Seu grupo de risco é 1")


