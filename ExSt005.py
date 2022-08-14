#Algoritimo While
import os

Contador = 1
SalarioMinimo = 450.00

Laco1 = True
Laco2 = True
while Contador <= 10:
    Codigo = (int(input("Digite o codigo do funcionário: ")))
    HoraTrabalhada = (float(input("Digite o número de horas trabalhadas: ")))
    while Laco1:
        print("O - Operário")
        print("G - Gerente")
        Categoria = (str(input("Informe a categoria: ")))
        if Categoria == "O" or Categoria == "G":
            Laco1 = False
        else:
            print("As categorias possiveis são O ou G, Digite novamente...")
            os.system(cls)
            continue

    while Laco2:
        print("M - Matutino")
        print("V - Vespertino")
        print("N - Noturno")
        Turno = (str(input("Informe o turno: ")))
        if Turno == "O" or Turno == "G":
            Laco2 = False
        else:
            print("Os Turnos possiveis são M, V ou N, Digite novamente...")
        continue








    if Categoria == "O":
        if Turno == "M" or Turno == "V":
           ValorHora = SalarioMinimo * 0.10

        elif Turno == "N":
            ValorHora = SalarioMinimo * 0.13
        else:
            print("Informe o turno corretamente")
            continue
    elif Categoria == "G":
        if Turno == "M" or Turno == "V":
           ValorHora = SalarioMinimo * 0.15
        elif Turno == "N":
            ValorHora = SalarioMinimo * 0.18
        else:
            print("Informe o turno corretamente")
            continue

    else:
        print("Informe a categoria corretamente")
        continue

    SalarioInicial = HoraTrabalhada * ValorHora
    if SalarioInicial <= 300.00:
        AuxilioAlimen = SalarioInicial * 0.20
    elif SalarioInicial > 300.00 and SalarioInicial <= 600.00:
        AuxilioAlimen = SalarioInicial * 0.15
    else:
        AuxilioAlimen = SalarioInicial * 0.05

    SalarioFinal = SalarioInicial + AuxilioAlimen

    print("Codigo:", Codigo, "Horas Trabalhadas: ", HoraTrabalhada, "Salario Inicial:", SalarioInicial)

    print("Auxilio Alimentação: R$", AuxilioAlimen, "Salario Final: R$", SalarioFinal)

    Escreva("Contagem", Contador, "/ 10");
    Contador = Contador + 1

print("Fim do programa.")









