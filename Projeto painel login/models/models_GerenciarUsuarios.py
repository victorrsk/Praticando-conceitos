import json
import os
from models_Usuario import Usuario

class GerenciarUsuarios:
    
    def __init__(self, arquivo_usuarios):
        self.arquivo_usuarios = arquivo_usuarios
        self.usuarios = []
        
    def carregar_usuarios(self):
        # deve ser chamado para carregar os dados do JSON, caso contrario o conteudo será sobrescrito
        try:
            # se o arquivo já existe, abre e carrega os dados do JSON
            with open(self.arquivo_usuarios, 'r', encoding='utf-8') as arquivo_usuarios:
                self.usuarios = json.load(arquivo_usuarios)
        
        # tratamento de erros     
        except FileNotFoundError as exc:
            print(f'O arquivo não existe: {exc}')
            # cria o arquivo caso o mesmo não exista
            if (resp := input('Deseja criar o arquivo?: ')).upper().strip() == 'S':
                with open(self.arquivo_usuarios, 'x') as arquivo:
                    print('Arquivo criado com sucesso')
        
        except json.decoder.JSONDecodeError as exc:
            # trata o erro ao tentar abrir um JSON vazio
            print(f'O arquivo JSON está vazio: {exc}')
            print('Consertando...')
            with open(self.arquivo_usuarios, 'w') as arquivo_usuarios:
                # insere um par de colchetes no arquivo para evitar o erro
                arquivo_usuarios.write(f'{[]}')
      
    def salvar_usuarios(self):
        try:
            with open(self.arquivo_usuarios, 'w', encoding='utf-8') as arquivo_usuarios:
                json.dump(self.usuarios, arquivo_usuarios, indent=4, ensure_ascii=False)
        except IOError:
            print('Algum erro aconteceu')
          
    def cadastrar(self, nome, email, senha):
        obj_usuario = Usuario(nome=nome, email=email, senha=senha)
        # adiciona os dados do usuario a lista de usuarios
        # to_dict transforma o objeto em dicionário
        self.usuarios.append(obj_usuario.to_dict()) 
    
