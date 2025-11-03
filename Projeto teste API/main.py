from funcoes import get_post, get_posts, delete_post, post_post, patch_post_title
from cli import interface

while True:
    interface()
    escolha = input('Opção desejada: ')
    
    if escolha == '1':
        qnt_posts = input('Quantidade de posts desejados: ')
        try:
            get_posts(int(qnt_posts))
        except ValueError:
            print('Tipo inválido')

    elif escolha == '2':
        id_post = input('ID do post: ')
        try:
            get_post(int(id_post))
        except ValueError:
            print('Tipo inválido')

    elif escolha == '3':
        # os dados do post serão inseridos dentro da função
        post_post()

    elif escolha == '4':
        id_post = input('ID do post: ')
        try:
            patch_post_title(int(id_post))
        except ValueError:
            print('Tipo inválido')

    elif escolha == '5':
        id_post = input('ID do post: ')
        try:
            delete_post(int(id_post))
        except ValueError:
            print('Tipo inválido')

    elif escolha == '6':
        print('Encerrando')
        break

    else:
        print('Opção inválida')

    print()