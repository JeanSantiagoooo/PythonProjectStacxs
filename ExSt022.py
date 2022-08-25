"""
Faça um programa para calcular a tabuada de qualquer número digitado pelo usuário.
"""
Numero = int(input("Digite o numero que deseja saber a tabuada: "))
i = 1
Tabuada = 1

for i in range (10):
    if Numero > 0:
        Resultado = Numero * Tabuada
        print(Numero, "X", Tabuada, "=", Resultado)
        Tabuada += 1
    else:
        if Numero == 0:
            print("Qualquer número multiplicado por 0 é igual a 0")
            break
        else:
            print("Digite apenas números positivos")
            break