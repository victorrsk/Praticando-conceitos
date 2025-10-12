def menu():
    print('Serviço Streaming'.center(29, '-'))
    print()
    print('\t1-ASSISTIR\n\t2-ADICIONAR FILME/ SERIE\n\t3-LISTAR FILMES/ SERIES\n')

def validar_email(email):
    import re

    padrao = r'[a-zA-Z]{2,}[0-9]*(@){1}(gmail.com){1}'

    if re.match(padrao, email):
        return True
    else:
        return False


def validar_nome(nome):
    import re
    
    padrao = r'[a-zA-Z]{3,}'
    
    if re.fullmatch(padrao, nome):
        return True
    else:
        return False
    
       
def menu_cadastro():
    nome = input('Informe o nome do usuário: ')
    nome_valido = validar_nome(nome)
    
    if not nome_valido:
        return 'Nome inválido, cadastro cancelado'
    else:
        email = input('Informe o e-mail do usuário: ')
        email_valido = validar_email(email)
        
        if email_valido:
            print('Conta criada com sucesso')
            return True
        else:
            print('E-mail inválido, cadastro cancelado')
            return False

    
    
print(menu_cadastro())