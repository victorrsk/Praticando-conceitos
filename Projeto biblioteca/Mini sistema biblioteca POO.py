# sistema de biblioteca
# - os livros precisam ter titulo, autor, disponivel <- bool
# - classe pessoa

class Livro:

    def __init__(self, titulo, autor, disponivel=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = disponivel

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def disponivel(self):
        return self.__disponivel

    def __str__(self):
        return f'TITULO: {self.__titulo}\nAUTOR: {self.__autor}\nDISPONIVEL: {'SIM' if self.__disponivel else 'NÃO'}'

    def emprestar(self):
        self.__disponivel = False
        return

    def devolver(self):
        self.__disponivel = True
        return


class Pessoa:

    def __init__(self, nome):
        self.__nome = nome
        self._livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.disponivel:
            self._livros_emprestados.append(livro.titulo)
            livro.emprestar()
            return f'{self.__nome} emprestou {livro.titulo} 🚶‍➡️'
        
        return f'O livro "{livro.titulo}" não está disponivel'
        
    def devolver_livro(self, livro):
        if not livro.disponivel:
            self._livros_emprestados.remove(livro.titulo)
            livro.devolver()
            return f'O livro "{livro.titulo}" foi devolvido'
        
        return f'O livro "{livro.titulo}" já está disponível'
    
    @property
    def livros_emprestados(self):
        return self._livros_emprestados
    
    
# livros
One_Piece = Livro('One Piece', 'Oda')
Dom_Casmurro = Livro('Dom Casmurro', 'Machado de Assis')
A_Metamorfose = Livro('A Metamorfose', 'Franz Kafka')


# objeto pessoa
Victor = Pessoa('Victor')

# testes
print(f'O livro está disponivel?: {One_Piece.disponivel}')

# emprestando o livro
print(Victor.emprestar_livro(One_Piece))
print(f'O livro está disponivel?: {One_Piece.disponivel}')

# devolvendo o livro
print(Victor.devolver_livro(Dom_Casmurro))
print(Victor.livros_emprestados)