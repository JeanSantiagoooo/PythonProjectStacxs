# Algorítimo 003: Operações com tipos basicos
# Dev: Jean Santiago
# Data: 19.08.2022
'''''''''
x = 1
y = 2

resultado = x + y
print(resultado)
print(type(resultado))

# pontos flutuantes
x = 2.2
y = 5.9

resultado = x + y
print(resultado)
print(type(resultado))

# número inteiro e pontos flutuantes
x = 2
y = 5.9

resultado = x + y
print(resultado)
print(type(resultado))

# conversão de tipos

x = 10
s = str(x)
print(s)
print(type(s))

# de float para inteiro
x = 90.23
b = int(x)
print(b)
print(type(b))

# de inteiro para flutuante
x = 70
b = float(x)
print(b)
print(type(b))

# string

StringVazia = ''
UmaLetra = 'a'
VariasLetras = 'Banana'

print(type(StringVazia))
print(type(UmaLetra))
print(type(VariasLetras))

t = 'var'
p = t
print(t)
print(p)


a = True
print(type(a))

a = 4 > 3
print(a)

b = 'laranja' > 'limão'
print(b)

b = 'laranja' == 'laranja'
print(b)

x = y = 7
print(x <= y and y <= x)
'''''
n = 6
fatorial = 1
while n > 1:
    fatorial *= n
    n -= 1
    print(fatorial)