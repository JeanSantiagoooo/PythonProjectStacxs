#swith case

TotalNota = Desconto = ValorFinal = quantidade = 0

Codigo = int(input("Digite o código do produto: "))
Quantidade = int(input("Digite a quantidade comprada: "))
if Codigo >=1 and Codigo <=10:
    Preco = 10.00
    TotalNota = Quantidade * Preco
    if TotalNota <= 250:
        Desconto = TotalNota * 0.05
        ValorFinal = TotalNota - Desconto
        print("Preço unitário: R$", Preco)
        print("Total da nota: R$", TotalNota)
        print("Valor de desconto: R$", Desconto)
        print("Valor final: R$", ValorFinal)
    else:
        print("O total da nota é: R$", TotalNota)

elif Codigo > 10 and Codigo <= 20:
    Preco = 15.00
    TotalNota = Quantidade * Preco
    if TotalNota > 250 and TotalNota <= 500:
        Desconto = TotalNota * 0.10
        ValorFinal = TotalNota - Desconto
        print("Preço unitário: R$", Preco)
        print("Total da nota: R$", TotalNota)
        print("Valor de desconto: R$", Desconto)
        print("Valor final: R$", ValorFinal)
    else:
        print("O total da nota é: R$", TotalNota)

elif Codigo > 20 and Codigo <=30:
    Preco = 20.00
    TotalNota = Quantidade * Preco
    if TotalNota > 50:
        Desconto = TotalNota * 0.15
        ValorFinal = TotalNota - Desconto
        print("Preço unitário: R$", Preco)
        print("Total da nota: R$", TotalNota)
        print("Valor de desconto: R$", Desconto)
        print("Valor final: R$", ValorFinal)
    else:
        print("O total da nota é: R$", TotalNota)

elif Codigo > 30 and Codigo <= 40:
    Preco = 30.00
    TotalNota = Quantidade * Preco
    ValorFinal = TotalNota
    print("Preço unitário: R$", Preco)
    print("Total da nota: R$", TotalNota)
    print("Valor de desconto: R$", Desconto)
    print("Valor final: R$", ValorFinal)

else:
    print("Informação inválida")
