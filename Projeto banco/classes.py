from random import randint
from abc import ABC, abstractmethod, abstractproperty

# criacao da interface Transacao
class Transacao(ABC):
    
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(conta):
        pass

class Deposito(Transacao):
    
    def __init__(self, valor):
        self.__valor = valor
        
    @property
    def valor(self):
        return self.__valor
        
    def registrar(self, conta):
        transacao_valida = conta.depositar(self.valor)
        
        if transacao_valida:
            conta.historico.adicionar_transacao(self)
    
class Saque(Transacao):
    
    def __init__(self, valor):
        self.__valor = valor
        
    @property
    def valor(self):
        return self.__valor
        
    def registrar(self, conta):
        transacao_valida = conta.sacar(self.valor)
        
        if transacao_valida:
            conta.historico.adicionar_transacao(self)
    
class Cliente:
    
    def __init__(self, endereco):
        self.__contas = []
        self.__endereco = endereco
        
    def adicionar_conta(self, conta):
        self.__contas.append(conta)
    
class Conta:
    
    # os outros atributos são setados em tempo de execução
    def __init__(self, cliente):
        self.__saldo = 0
        self.__numero = randint(1000, 2000)
        self.__agencia = 'Banco Padrao'
        self.__cliente = cliente # obj da classe cliente
        self.__historico = Historico() # obj da classe cliente
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def historico(self):
        return self.__historico
    
    @classmethod
    def nova_conta(cls, cliente):
        # método contrutor de objs Conta
        return cls(cliente)
    
    def __str__(self):
        return f'saldo: {self.__saldo}\nnumero: {self.__numero}\nagencia: {self.__agencia}\ncliente: {self.__cliente}'
    
    # métodos sacar e depositar tratam erros de tipo de dado, valor de saque maior que o saldo, valor de saque ou deposito negativo ou igual a zero
    def sacar(self, valor=0):
        
        if valor > self.__saldo:
            print('O valor excede o saldo da conta!')
            return False
            
        elif valor > 0:
            self.__saldo -= valor
            print('Saque realizado')
            return True
            
        else:
            print('O valor informado é inválido')
            return False

    
    def depositar(self, valor=0):
        
        if valor > 0:
            self.__saldo += valor
            print('Depósito realizado')
            return True
        else:
            print('O valor informado é inválido')
            return False
        
class ContaCorrente(Conta):
    
    def __init__(self, cliente, limite=500, limite_saques=3):
        super().__init__(cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        qnt_saques = 0
        saldo = self.saldo
        
        try:
            valor = float(valor)
        
            if valor > saldo and valor > self.limite:
                print('O valor excede o saldo e o limite da conta')
                
            elif valor > self.limite:
                print('O valor excede o limite')
            
            else:
                return super().sacar(valor)
            
            return False
        
        except ValueError:
            print('O tipo informado é inválido')
            return False
    
    def depositar(self, valor):
        
        try:
            valor = int(valor)
            
            if valor > 0:
                return super().depositar(valor)
            
            else:
                print('valor inválido')
                
            return False
        
        except ValueError:
            print('O tipo informado é inválido')
            return False
              
class Historico:
    
    def __init__(self):
        self.__transacoes = []
        
    def adicionar_transacao(self, transacao):
        self.__transacoes.append({'Tipo': transacao.__class__.__name__,
                                  'Valor': transacao.valor,
                                  'Data': 'desprezivel por agr'})