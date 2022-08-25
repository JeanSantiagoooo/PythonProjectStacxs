"""
Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1: feminino 2: masculino)
de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:

para homens: (72.7 * Altura) – 58
para mulheres: (62.1 * Altura) – 44.7
"""
Altura = float(input("Digite a altura: "))
print("1 - Feminino")
print("2 - Masculino")
Sexo = int(input("Informe o sexo: "))

if Sexo == 1:
    PesoIdeal = (62.1 * Altura) - 44.7
    print("O peso ideal, de acordo com seu sexo, é: ", PesoIdeal)
elif Sexo == 2:
    PesoIdeal = (72.7 * Altura) - 58
    print("O peso ideal, de acordo com seu sexo, é: ", PesoIdeal)

else:
    print("Insira as informações corretamente! FIM DO PROGRAMA")
