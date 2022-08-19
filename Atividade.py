# Algoritimo 001: Gratificação de natal
# Jean Santiago
# Data: 12/08/2022
# Uso de bibliotecas

import math

print(math.sqrt(81))
print(math.pow(2, 2))
print(2 ** 2)
print(divmod(20, 6))
print(20//6)  # Div
print(20 % 6)  # Mod

# soma e subtração
print(10 + 2 + 7)

# Potência
print(2 ^ 4)

# Divisão
print(20 / 6)
print(20 / 2)

# Precedência de operadores
# a ** 2 + b * 3 % 2, sendo a = 4 e b = 3
# 1. a ** 2 + b * 3 % 2
# 2. 4 ** 2 + 3 * 3 % 2
# 3. 16 + 3 * 3 % 2
# 4. 16 + 9 % 2
# 5. 16 + 1
# 6. 17
print(4 ** 2 + 3 * 3 % 2)

# Operadores lógicos: AND (E)
print(5 >= 5 and 4 < 5)  # True AND True = True
print(5 == 5 and 5 > 9)  # True AND False = False
print(5 == 5 and 5 >= 4)   # True AND True = True
print(5 == 4 and 5 >= 7)  # False AND False = False

# Operadores lógicos: OR (OU)
print(5 >= 5 or 4 < 5)  # True or True = True
print(5 >= 5 and 4 > 5)  # True or False = True
print(5 == 4 and 5 >= 4)  # True or false = True
print(5 == 4 and 5 == 7)  # False or False = False

# Operadores lógicos: NOT (NÃO)
print(not 5 == 4)  # (Not True = False) É falso que 5 é igual a 4
print(not 5 > 4)  # (Not True = False)  É True que 5 é maior que 4
print(not 4 > 5)  # (Not False = True)

# Operadores Relacionais
# == True, se A e B são iguais
print(77 == 77)  #True
print(77 == 76)  #False

# != True, se A e B são diferentes
print(77 != 77)  #False

# > True, se A é maior que B são diferentes
print(77 > 9)  #True

# >, <, >=, <=
print(77 > 9)  # True
print(7 > 9)   # False
print(7 < 9)   # True
print(7 <= 9)  # True
print(7 <= 7)  # True
print(7 >= 7)  # True
print(7 >= 10) # False

# Operadores de atribução
# = dade uma varmen que quer atribuir um valor

x = 90
print(x)
# incrementar +=
x += 2
print(x)
#Decrementar -=
x -= 10
print(x)
#divisão x 10 /=
x /= 10
print(x)
#Div x 10 //=
x = 20
x //= 10
print(x)

#Mod x 10 //=
x = 20
x %= 10
print(x)

# Multiplicção x 10 *=
x = 20
x *= 10
print(x)

print(2 + 3 * 5 + 30 // 10)





