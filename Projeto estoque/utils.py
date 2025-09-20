
def adicionar_produto(lista_produtos):
    import re
    padrao_codigo_produto = r'^[A-Z]{1}[0-9]{5}'
    codigo_produto = input('Informe o código do produto: ')
    
    if re.match(padrao_codigo_produto, codigo_produto):
        nome_produto = input('Informe o nome do produto: ')
        
        lista_produtos.append({'nome': nome_produto, 'codigo': codigo_produto})
        return f'Produto "{nome_produto}" cadastrado com sucesso'
    else:
        return 'Código inválido'
    
def sobrescrever_dados(lista):
    import json
    
    with open("Projeto estoque\\dados_estoque.json", 'w', encoding='utf-8') as dados_estoque:
        json.dump(lista, dados_estoque, indent=4, ensure_ascii=False)
        
def menu():
    
    print('--------GERENCIAMENTO ESTOQUE--------')
    print('1-Adicionar produto\n2-Remover produto\n0-Sair')
    
def remover_produto(lista_produtos):
    import re
    padrao_codigo_produto = r'^[A-Z]{1}[0-9]{5}'
    codigo_produto = input('Informe o código do produto: ')
    
    if re.match(padrao_codigo_produto, codigo_produto):
        for produto in lista_produtos:
            if produto['codigo'] == codigo_produto:
                return f'{produto['nome']} removido com sucesso'
    else:
        return 'O código informado é inválido ou não existe'
    
