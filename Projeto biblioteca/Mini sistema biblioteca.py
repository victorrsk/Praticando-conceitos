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


# livros
One_Piece = Livro('One Piece', 'Oda')
Dom_Casmurro = Livro('Dom Casmurro', 'Machado de Assis')
A_Metamorfose = Livro('A Metamorfose', 'Franz Kafka')

# testando disponibilidade antes de emprestar
print(One_Piece.disponivel)

Victor = Pessoa('Victor')
print(Victor.emprestar_livro(One_Piece))

# testando disponibilidade depos de emprestar
print(One_Piece.disponivel)
print(Victor.devolver_livro(One_Piece))
print(One_Piece.disponivel)
