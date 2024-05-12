# List comprehension em Python
# Lis comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

import pprint


lista = []
for numero in range(10):
    lista.append(numero)

lista = [numero * 2 for numero in range(10)]
#print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },

]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

lista = [n for n in range(10) if n < 5]
print(lista)