class Usuario:
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.__email = email
        self.__senha = senha
        
    @property
    def senha(self):
        return self.__senha
    @property
    def email(self):
        return self.__email
    
    def to_dict(self):
        # retorna o objeto na sintaxe do JSON
        return {'nome': self.nome, 'email': self.email, 'senha': self.senha}
    
    @property
    def exibir_info(self):
        print(f'-----Informações Usuário-----\n\tNome: {self.nome}\n\tEmail: {self.email}\n\tSenha: {self.senha}')
        
