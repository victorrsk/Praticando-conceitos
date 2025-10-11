from abc import ABC, abstractmethod, abstractproperty


# feito
class Usuario:
    
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email
        self.biblioteca = Biblioteca()
        
    @property
    def email(self):
        return self.__email
    
    def assistir(self, conteudo):
        return conteudo.reproduzir
    
    def adicionar_a_biblioteca(self, conteudo):
        self.biblioteca.adicionar_conteudo(conteudo)
        
class Biblioteca:
    
    def __init__(self):
        self.__conteudos = []
    
    @property
    def conteudos(self):
        return self.__conteudos
        
    def adicionar_conteudo(self, conteudo):
        self.__conteudos.append(
            {
            'titulo': conteudo.titulo,
            'duração': conteudo.duracao
            }
        )
    
    def listar_conteudos(self):
        return [conteudo for conteudo in self.__conteudos]


class Conteudo(ABC):
    
    def __init__(self, titulo, duracao, classificacao):
        super().__init__()
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao
    
    @abstractmethod
    def reproduzir(self):
        pass
    
    
class Filme(Conteudo):
    
    def __init__(self, titulo, duracao, classificacao, diretor):
        super().__init__(titulo, duracao, classificacao)
        self.diretor = diretor

    @property
    def reproduzir(self):
        return f'Assistindo a "{self.titulo}"'


class Serie(Conteudo):

    def __init__(self, titulo, duracao, classificacao, temporadas, episodios):
        super().__init__(titulo, duracao, classificacao)
        self.temporadas = temporadas
        self.episodios = episodios
    
    @property
    def reproduzir(self):
        return f'Assistindo a "{self.titulo}"'


    
user = Usuario('Victor', 'jv191207@gmail.com')
filme = Filme('Bosta', 2.45, 18, 'Carlinhos')

user.adicionar_a_biblioteca(filme)

print(user.assistir(filme))
