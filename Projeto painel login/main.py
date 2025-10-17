from models.models_GerenciarUsuarios import GerenciarUsuarios
from models.models_Interface import menu, validar_dados

gerenciar_usuarios = GerenciarUsuarios('users_data.json')
usuarios_carregados = gerenciar_usuarios.carregar_usuarios() # carregando os dados do JSON
gerenciar_usuarios.carregar_usuarios() # meio armengado, mas isso serve pra inserir [] no JSON vazio

if usuarios_carregados:
    while True:
        menu()

        resp = input('Sua escolha: ')
        
        if resp == '1':
            nome = input('Seu nome: ')
            email = input('Seu email: ')
            senha = input('Sua senha: ')
            # verifica os dados em funções no arquivo de interface
            dados_validos = validar_dados(nome, email, senha)
            # se todos forem validos, cadastra o usuario
            if dados_validos:
                gerenciar_usuarios.cadastrar(nome, email, senha)
                print('Usuario cadastrado com sucesso!')
            else:
                print('Deu merda')
                
