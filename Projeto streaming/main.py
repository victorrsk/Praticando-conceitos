from classes import Usuario, lista_filmes, lista_series, Filme, Serie
from interface import menu, menu_cadastro, serie_ou_filme
from time import sleep

usuario_cadastrado = menu_cadastro()

if bool(usuario_cadastrado):

    while True:
        
        # puxando filme e serie aleatorio
        filme = lista_filmes()
        serie = lista_series()

        menu()

        opcao = input('Opção desejada: ')

        # o filme/ serie que vai ser assistido, tanto faz, aleatorio aqui
        if opcao == '1':
            # se True, serie, se False, filme
            tipo_conteudo = serie_ou_filme()

            if tipo_conteudo:
                print(usuario_cadastrado.assistir(serie))

            elif not tipo_conteudo:
                print(usuario_cadastrado.assistir(filme))

        elif opcao == '2':
            # se True, serie, se False, filme
            tipo_conteudo = serie_ou_filme()

            if tipo_conteudo:
                usuario_cadastrado.adicionar_a_biblioteca(serie)
            elif not tipo_conteudo:
                usuario_cadastrado.adicionar_a_biblioteca(filme)
        # mostra os assistidos
        elif opcao == '3':
            print(usuario_cadastrado.historico.assistidos)
        
        #TODO opcao 4 que mostra não o historico mas sim os conteudos da biblioteca

        elif opcao == 'q':
            break
        
        else:
            print('Opção inválida')
        
        print()

# teste
if usuario_cadastrado:        
    print(usuario_cadastrado.historico.assistidos)
    print(usuario_cadastrado.biblioteca.listar_conteudos)
    print(usuario_cadastrado.historico.listar_historico)