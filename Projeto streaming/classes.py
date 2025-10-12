from abc import ABC, abstractmethod, abstractproperty
from random import choice

# feito
class Usuario:
    
    def __init__(self, nome, email):
        self.nome = nome
        self.__email = email
        self.biblioteca = Biblioteca()
        self.historico = Historico()
        
    @property
    def email(self):
        return self.__email
    
    def assistir(self, conteudo):
        self.historico.registrar(conteudo)
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
    
    @property
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


class Historico:
    
    def __init__(self):
        self.assistidos = []
        
    def registrar(self, conteudo):
        self.assistidos.append(conteudo.titulo)
    
    @property
    def listar_historico(self):
        return [f'{indice+1}-{titulo}' for indice, titulo in enumerate(self.assistidos)]
    
    

# filmes teste
filmes = [
    Filme("O Grande Truque", 130, "Christopher Nolan", 14),
    Filme("A Origem", 148, "Christopher Nolan", 14),
    Filme("Gladiador", 155, "Ridley Scott", 16),
    Filme("Forrest Gump", 142, "Robert Zemeckis", 12),
    Filme("O Resgate do Soldado Ryan", 169, "Steven Spielberg", 16),
    Filme("O Senhor dos Anéis: A Sociedade do Anel", 178, "Peter Jackson", 12),
    Filme("O Poderoso Chefão", 175, "Francis Ford Coppola", 18),
    Filme("Bastardos Inglórios", 153, "Quentin Tarantino", 18),
    Filme("Matrix", 136, "Lana e Lilly Wachowski", 16),
    Filme("O Lobo de Wall Street", 180, "Martin Scorsese", 18)
]

# series teste
series = [
    Serie("Breaking Bad", 47, 5, 62, 18),
    Serie("Stranger Things", 50, 4, 34, 14),
    Serie("Game of Thrones", 55, 8, 73, 18),
    Serie("The Office", 22, 9, 201, 12),
    Serie("The Witcher", 60, 3, 24, 16),
    Serie("Dark", 55, 3, 26, 16),
    Serie("Sherlock", 90, 4, 13, 14),
    Serie("Peaky Blinders", 58, 6, 36, 18),
    Serie("Friends", 23, 10, 236, 12),
    Serie("The Boys", 60, 4, 32, 18)
]

user = Usuario('Victor', 'jv191207@gmail.com')
