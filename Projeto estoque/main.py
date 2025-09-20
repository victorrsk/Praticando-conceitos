from utils import adicionar_produto, sobrescrever_dados, menu, remover_produto
import json

while True:
    menu()
    
    escolha = input('Informe a opção desejada: ').strip()
    try:
        escolha = int(escolha)
        if escolha == 1: 
            try:
                with open("Projeto estoque\\dados_estoque.json", 'r', encoding='utf-8') as dados_arquivos:
                    lista_produtos = json.load(dados_arquivos)
            except:
                print('Arquivo vazio, lista criada')
                lista_produtos = []
                
            qnt_produtos = input('Quantidade de produtos desejada: ')
                
            try:
                qnt_produtos = int(qnt_produtos)
                for i in range(qnt_produtos):
                    print(adicionar_produto(lista_produtos))
                sobrescrever_dados(lista_produtos)
            except:
                print('O valor informado é inválido')
                
        elif escolha == 2:
            remover_produto()
        elif escolha == 0:
            break
        else:
            print('Opção inválida 🛠️⚙️')
    except:
        print('Valor inválido 🛠️⚙️')