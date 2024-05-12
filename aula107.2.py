# Primeiro, defina uma função que pode multiplicar um número por qualquer outro número

def multiply(n, multiplier):
    return n * multiplier

# Agora, vamos definir alguns números para testar a função

numbers = [1, 2, 3, 4, 5]

# E os multiplicadores que queremos usar

multipliers = [2, 3, 4]

# Para cada número na lista 'numbers', vamos chamar a função com cada multiplicador e imprimir
# os resultados

for num in numbers:
    for multiplier in multipliers:
        print(f'{multiplier} times {num} is {multiply(num, multiplier)}')
    print('---')