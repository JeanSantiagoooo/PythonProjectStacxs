"""
 Escreva um programa que verifique a validade de uma senha fornecida pelo usuário.
 A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
 ACESSO PERMITIDO caso a senha seja válida e  ACESSO NEGADO caso a senha seja inválida.
"""
SenhaCorreta = "1234"
Senha = int(input("Digite a senha: "))

if Senha == SenhaCorreta:
    print("ACESSO PERMITIDO")
elif Senha != SenhaCorreta:
    print("ACESSO NEGADO")


