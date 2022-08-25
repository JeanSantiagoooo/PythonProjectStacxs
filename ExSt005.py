#Algoritimo While

Contador = 1
SalarioMinimo = 450.00


Laco1 = True
Laco2 = True
while Contador <= 10:
    SalarioInicial = 0
    AuxilioAlimentacao = 0
    SalarioFinal = 0

    Codigo = input("Digite o codigo do funcionário: ")
    HoraTrabalhada = (float(input("Digite o número de horas trabalhadas: ")))
    while Laco1:
        print("O - Operário")
        print("G - Gerente")
        Categoria = str(input("Informe a categoria: "))
        if Categoria == "O" or Categoria == "G":
            Laco1 = False
        else:
            print("Apenas letras maiusculas O ou G, digite novamente...")
            continue

    while Laco2:
        print("M - Matutino")
        print("V - Vespertino")
        print("N - Noturno")
        Turno = input("Informe o turno: ")

        if Turno == "M" or Turno == "V" or Turno == "N":
            Laco2 = False
        else:
            print("Os Turnos possiveis são M, V ou N, Digite novamente...")
            continue

    if Categoria == "G" and Turno == "N":
        ValorHora = SalarioMinimo * 0.18
        SalarioInicial = ValorHora * HoraTrabalhada
        if SalarioInicial < 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial >= 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    elif Categoria == "G" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.15
        SalarioInicial = ValorHora * HoraTrabalhada
        if SalarioInicial < 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial >= 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    elif Categoria == "O" and Turno == "N":
        ValorHora = SalarioMinimo * 0.13
        SalarioInicial = ValorHora * HoraTrabalhada
        if SalarioInicial < 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial >= 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    elif Categoria == "O" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.10
        SalarioInicial = ValorHora * HoraTrabalhada
        if SalarioInicial < 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial >= 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    print("Codigo:", Codigo, "Horas Trabalhadas: ", HoraTrabalhada, "Salario Inicial:", SalarioInicial, )

    print("Auxilio Alimentação:", AuxilioAlimentacao, "Salario Final: ", SalarioFinal)

    print("Contador", Contador)
    Contador += 1
    Laco1 = True
    Laco2 = True
print("Fim do programa.")













