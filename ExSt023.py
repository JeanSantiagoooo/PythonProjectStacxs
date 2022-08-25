Categoria = 0

Preco = float(input("Digite o preço do produto: "))
Laco1 = True
Laco2 = True
while Laco1:
    print("1 - Limpeza")
    print("2 - Alimentação")
    print("3 - Vestuário")
    Categoria = int(input("Escolha a categoria: "))
    if Categoria == 1 or Categoria == 2 or Categoria == 3:
        Laco1 = False
    else:
        continue
while Laco2:
    print("R – produtos que necessitam de refrigeração")
    print("N – produtos que não necessitam de refrigeração")
    Situacao = str(input("Escolha Situação: "))
    if Situacao == "R" or Situacao == "N":
        Laco2 = False
    else:
        continue

print("Categoria:", Categoria)
print("Situação:", Situacao)
print("Valor inicial: R$",Preco)
Aumento = 0

if Categoria == 1:
    if Preco <= 25:
        Aumento = Preco * 0.05
    else:
        Aumento = Preco * 0.12
elif Categoria == 2:
    if Preco <= 25:
        Aumento = Preco * 0.08
    else:
        Aumento = Preco * 0.15
else:
    if Preco <= 25:
        Aumento = Preco * 0.10
    else:
        Aumento = Preco * 0.18

Valor = Aumento + Preco
print("Valor do Aumento: R$", round(Aumento,2), "\ Total: R$", round(Valor,2))

if Situacao == "R" or Categoria == 2:
    Imposto = Valor * 0.05
    NovoPreco = Valor - Imposto
    print("Impostos: R$",round(Imposto,2))
    print("Novo preço: R$", round(NovoPreco, 2))
else:
    Imposto = Valor * 0.08
    NovoPreco = Valor - Imposto
    print("Impostos: R$",round(Imposto,2))
    print("Novo preço: R$", round(NovoPreco, 2))

if NovoPreco <= 50:
    print("Produdo Barato")
elif NovoPreco > 50 and NovoPreco <= 120:
    print("Preço Normal")
else:
    print("Produto Caro")
