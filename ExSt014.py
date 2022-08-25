"""
Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).

Calcular e imprimir o seguinte:

Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área

Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.

Se o número de lados for igual a 5 escrever PENTÁGONO.

Obs: O foco aqui é a lógica com o comando de controle IF, demais conhecimentos envolvidos pesquise mais.
"""
Lados = int(input("Digite o número de lados do polígono: "))
Base = float(input("Digite o valor da base, em cm:"))
Altura = float(input("Digite o valor da altura, em cm:"))

if Lados == 3:
    print("A figura é um TRIÂNDULO")
    Area = (Base * Altura) / 2
    print("O valor da área é: ", Area)
elif Lados == 4:
    print("A figura é um QUADRADO")
    Area = Base * Altura
    print("O valor da área é: ", Area)
elif Lados == 5:
    print("A figura é um PENTAGONO")

