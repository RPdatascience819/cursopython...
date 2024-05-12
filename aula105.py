
# Exercícios com funções

# Crie uma função que multiplica todos os argumentos, não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

result = multiply(2, 3, 4, 5)
print(f"O resultado da multiplicação é: {result}")

# Crie uma função fala se o número é par ou impar.
# Retorne se o número é par ou impar.

def par_ou_impar(n):
    if n % 2 == 0:
        return f'{n} é par'
    return f'{n} é impar'
    
print(par_ou_impar(7))
print(par_ou_impar(8))

