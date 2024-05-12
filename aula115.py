# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

#print(a, b)



# (a, b), (b1, b2) = pessoa.items()
# print(a, b)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'Sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
#print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

#mostro_argumentos_nomeados(nome= 'Joana', qualquer=123)
mostro_argumentos_nomeados(**pessoas_completa)