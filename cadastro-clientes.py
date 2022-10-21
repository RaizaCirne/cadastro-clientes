# Este programa pede ao usuário os dados pessoais de um cliente.
# Armazena os dados na memória RAM e exibe na tela os dados dos clientes cadastrados

nome = input('Digite o nome do cliente: ')
datanasc = input('Digite a data de nascimento: ')
endereco = input('Digite o endereço: ')
tel = input('Digite o telefone: ')

print('Cliente: {}\nData de nascimento {}\nTelefone: {}'.format(nome, datanasc, endereco, tel))
