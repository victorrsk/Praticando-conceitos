from utils import adicionar_produto, sobrescrever_dados, menu, remover_produto
import json

while True:
    # mostra o menu do sisteminha
    menu()
    # pergunta a opção desejada
    escolha = input('Informe a opção desejada: ').strip()
    try:
        escolha = int(escolha)
        # abre o arquivo dos dados do estoque e carrega os dados do json para a lista_produto
        if escolha == 1: 
            try:
                with open("Projeto estoque\\dados_estoque.json", 'r', encoding='utf-8') as dados_arquivos:
                    lista_produtos = json.load(dados_arquivos)
        # caso o arquivo esteja vazio, ele cria a lista aqui
            except:
                print('Arquivo vazio, lista criada')
                lista_produtos = []
        # le a quantidade de produtos a serem adicionados   
            qnt_produtos = input('Quantidade de produtos desejada: ')
                
            try:
                qnt_produtos = int(qnt_produtos)
        # o for faz o loop equivalente a quantidade de produtos
                for i in range(qnt_produtos):
                    print(adicionar_produto(lista_produtos))
        # sobrescreve os dados do arquivo mas agora com os novos produtos            
                sobrescrever_dados(lista_produtos)
            except:
                print('O valor informado é inválido')
                
        elif escolha == 2:
            remover_produto(lista_produtos)
        elif escolha == 0:
            break
        else:
            print('Opção inválida 🛠️⚙️')
    except:
        print('Valor inválido 🛠️⚙️')