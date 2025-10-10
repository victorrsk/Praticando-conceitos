from classes import ContaCorrente, Cliente

def menu():
    print('-----OPÇÕES-----\n1-CRIAR CONTA CORRENTE\nQ-SAIR')
    
    
resp = input('Resposta: ')

if resp == '1':
    cliente = ContaCorrente()
