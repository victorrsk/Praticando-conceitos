from classes import ContaCorrente


carlos = ContaCorrente.nova_conta('teste')

carlos.depositar(5000)
print(carlos.saldo)
carlos.sacar(200)
print(carlos.saldo)



