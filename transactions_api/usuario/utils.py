def validar_cpf(cpf):
    '''
        Metodo para validacao da estrutura de um cpf com base no algoritmo do modulo 11 \n
        Mais informacoes sobre o funcionamento do algoritmo: http://www.goulart.pro.br/cbasico/Calculo_dv.htm
    '''
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        raise ValueError('O CPF deve possuir 11 dígitos')
    
    # Calcula o primeiro digito verificador cpf[9]
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    resto = total % 11
    digito1 = 11 - resto if resto > 1 else 0

    # Calculo o segundo digito verificador cpf[10]
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    resto = total % 11
    digito2 = 11 - resto if resto > 1 else 0

    if not (int(cpf[9]) == digito1 and int(cpf[10]) == digito2):
        raise ValueError('CPF inválido')

    return cpf



def validar_cnpj(cnpj):
    # Remove caracteres não numéricos
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        raise ValueError('O CNPJ deve possuir 14 dígitos')

    # Calcula o primeiro dígito verificador
    total = 0
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(12):
        total += int(cnpj[i]) * pesos[i]
    resto = total % 11
    digito1 = 11 - resto if resto > 1 else 0

    # Calcula o segundo dígito verificador
    total = 0
    pesos.insert(0, 6)  # Adiciona o 6 à lista de pesos
    for i in range(13):
        total += int(cnpj[i]) * pesos[i]
    resto = total % 11
    digito2 = 11 - resto if resto > 1 else 0

    # Verifica se os dígitos verificadores estão corretos
    if not (int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2):
        raise ValueError('CNPJ inválido')

    return cnpj