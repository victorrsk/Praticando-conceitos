

# classe Conta
    # o atributo cliente é uma instancia da classe Cliente, feito
    # criar métodos nova_conta, sacar e depositar
    # conta corrente é a classe usada para criar definitivamente os objeots, feito

# padronizar o codigo com getters e setters
class Conta:
    
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.__saldo = saldo
        self.__numero = numero
        self.__agencia = agencia
        self.__cliente = cliente # obj da classe cliente
        self.__historico = historico # obj da classe historico
        
    @property
    def saldo(self):
        # getter do saldo
        return self.__saldo
    
    @property
    def cliente(self):
        # getter do cliente
        return self.__cliente
    

class ContaCorrente(Conta):
    # tudo feito aqui
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.__limite = limite
        self.__limite_saques = limite_saques


class Cliente:
    
    def __init__(self, endereco):
        self.__endereco = endereco
        self.__contas = []
        
    @property
    def contas(self):
        return self.__contas
    
    @property
    def endereco(self):
        return self.__endereco
    
    # método adicionar_conta e realizar_transação

class PessoaFisica(Cliente):
    # tudo feito aqui
    def __init__(self, cpf, nome, data_nasc):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nasc = data_nasc
    
    @property
    def CPF(self):
        return self.__cpf