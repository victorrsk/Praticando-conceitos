def menu():
    print('Serviço Streaming'.center(39, '-'))
    print()
    print('\t1-ASSISTIR\n\t2-ADICIONAR FILME/ SERIE\n\t3-LISTAR FILMES/ SERIES\n')

def validar_email(email):
    import re

    padrao = r'[a-zA-Z]{3,}[0-9]*(@){1}(gmail.com){1}'

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
    # cadastra o usuario caso o mesmo siga os padrões de nome e email
    from classes import Usuario
    # nome precisa de ao menos 3 letras
    nome = input('Informe o nome do usuário: ')
    nome_valido = validar_nome(nome)
    
    if not nome_valido:
        print('Nome inválido, cadastro cancelado')
        return False
    else:
        # email precisa de ao menos 3 letras, um @ e gmail.com
        email = input('Informe o e-mail do usuário: ')
        email_valido = validar_email(email)
        
        if email_valido:
            # caso o email seja válido, retorna um objeto Usuario
            print('Conta criada com sucesso')
            return Usuario(nome, email)
        else:
            print('E-mail inválido, cadastro cancelado')
            return False


def serie_ou_filme():
    # o retorno define o conteudo que será assistido ou adicionado a biblioteca do usuario
    tipo_conteudo = input('Serie ou filme?: ').strip().upper()
    
    if tipo_conteudo == 'SERIE':
        return True
    elif tipo_conteudo == 'FILME':
        return False
    else:
        return 'Opção inválida'
    
