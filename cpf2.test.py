

import random

def gerar_cpf():
    # Gera 9 dígitos aleatório
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro digito verificador
    soma = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
    resto = soma % 11

    if resto < 2:
        cpf.append(0)
    else:
        cpf.append(11 - resto)

    # Calcula o segundo dígito verificador
    soma = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
    resto = soma % 11
    if resto < 2:
        cpf.append(0)
    else:
        cpf.append(11 - resto)

    # Formata o CPF
    cpf_formatado = ''.join(map(str, cpf))
    cpf_formatado = cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

    return cpf_formatado

def validar_cpf(cpf):
    # Remove caracteres especiais do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(x) * y for x, y in zip(cpf[:9], range(10, 1, -1)))
    resto = soma % 11
    if resto < 2:
        digito_verificador = 0
    else:
        digito_verificador = 11 - resto
    if digito_verificador != int(cpf[9]):
        return False
    
    soma = sum(int(x) * y for x, y in zip(cpf[:10], range(11, 1, -1)))
    resto = soma % 11
    if resto < 2:
        digito_verificador = 0
    else:
        digito_verificador = 11 - resto
    if digito_verificador != int(cpf[10]):
        return False
    
    return True
    
    # Função para entrada do CPF
def entrada_cpf():
    escolha = input("Deseja gerar um CPF aleatório (S/N?) ").upper()
    if escolha == "S":
        print("CPF gerado com sucesso!")
        return gerar_cpf()
    elif escolha == "N":
        cpf = input("Digite o CPF (apenas números): ")
        if validar_cpf(cpf):
            print("CPF inserido pelo cliente:", cpf)
            return cpf
        else:
            print("CPF inválido!")
        return None
    else:
        print("Opção inválida!")
        return None
    
# Exemplo de uso
if __name__ == "__main__":
    cpf = entrada_cpf()
    if cpf:
        print("CPF Válido!:", cpf)

    
    