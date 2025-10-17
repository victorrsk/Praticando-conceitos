import re

def menu():
    print('--PAINEL USUÁRIO--')
    print('1-CADASTRAR\n2-ENTRAR\n3-SAIR')

def validar_email(email):

    padrao = r'[a-zA-Z]{2,}[0-9]*(@){1}(gmail.com){1}'

    if re.fullmatch(padrao, email):
        return True
    else:
        return False

def validar_nome(nome):

    padrao = r'[a-zA-Z]{3,}'
    
    if re.fullmatch(padrao, nome):
        return True
    else:
        return False
    
def validar_senha(senha):
    
    # padrao simples, 2 letras e 6 caracteres no minimo
    padrao = r'[a-zA-Z]{2,}[0-9]{6,}'
    
    if re.fullmatch(padrao, senha):
        return True
    else:
        return False
    
def validar_dados(nome, email, senha):
    nome_valido = validar_nome(nome)
    email_valido = validar_email(email)
    senha_valida = validar_senha(senha)
    
    if nome_valido and email_valido and senha_valida:
        return True
    
    return False