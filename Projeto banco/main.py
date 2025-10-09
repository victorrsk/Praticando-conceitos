from classes import ContaCorrente, Cliente, Conta, PessoaFisica

pessoa = ContaCorrente(0,
                       2020,
                       '0012',
                       Cliente('R. José Mauricio do Nasc'),
                       'teste',
                       1500,
                       3)

print(pessoa.cliente.endereco)





















