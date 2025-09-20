from utils import adicionar_produto, sobrescrever_dados
import json

# ter um menu para cadastrar e remover produtos
# tratar os dados vindos do arquivo como dicionarios <- JSON
# transformar isso em um REPO

try:
    with open("Projeto estoque\\dados_estoque.json", 'r', encoding='utf-8') as dados_arquivos:
        lista_produtos = json.load(dados_arquivos)
except:
    print('Arquivo vazio, lista criada')
    lista_produtos = []

for i in range(2):
    print(adicionar_produto(lista_produtos))

sobrescrever_dados(lista_produtos)

