"""
Tarefa FOR 1:

Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:

a) esse funcionário foi contratado em 2000, com salário inicial de R$1.000,00;

b) Em 2001, ele recebeu aumento de 1,5%, sobre o seu salário inicial;

c) A partir de 2002 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.

Faça um programa que determine o salário desse funcionário dos anos de 2000 à 2017. Apresente todos os valores.
"""
SalarioInicial = 0
PercentualAumento = 0
ReajusteSalarial = 0
SalarioAcumulado = 0
AnoInicial = 2000
AnoFinal = 2018

for i in range (AnoInicial,AnoFinal,1):

	if i == 2000:
		SalarioInicial = 1000.00
		print(i, "\ SI:",SalarioInicial)
	elif i == 2001:
		PercentualAumento = 0.015
		ReajusteSalarial = SalarioInicial * PercentualAumento
		SalarioAcumulado = ReajusteSalarial + SalarioInicial
		print(i, "\ SI:",SalarioInicial, "\ ",PercentualAumento,"%" "\ RS:(R$)",round(ReajusteSalarial,2), "\ SA:",round(SalarioAcumulado,2))
	else:
		print(i, "SA: ",round(SalarioAcumulado,2))
		ReajusteSalarial = SalarioAcumulado * PercentualAumento
		SalarioAcumulado = ReajusteSalarial + SalarioAcumulado
		print(i, "\ ",PercentualAumento,"%" "\ RS:(R$)",round(ReajusteSalarial,2), "\ SA:",round(SalarioAcumulado,2))
	PercentualAumento *=2
	i += 1
