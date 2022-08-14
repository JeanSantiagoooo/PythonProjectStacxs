# Algoritimo 001: Gratificação de natal
# Jean Santiago
# Data: 12/08/2022
# variaveis


HorasExtra = (float(input("Digite o numero de horas extras:")))
HorasFalta = (float(input("digite o numero de faltas:")))
MinutosTotal = ((HorasExtra) - (2/3*(HorasFalta))) * 60
print(MinutosTotal)
if(MinutosTotal > 2400):
    print("O seu premio é de R$ 500,00.")
elif(MinutosTotal >= 1801 and MinutosTotal <= 2400):
    print("O seu premio é de R$ 400,00.")
elif(MinutosTotal >= 1201 and MinutosTotal <= 1800):
    print("O seu premio é de R$ 300,00.")
elif(MinutosTotal > 600 and MinutosTotal <= 1201):
    print("O seu premio é de R$ 200,00.")
else:
    print("O seu premio é de R$ 100,00.")
