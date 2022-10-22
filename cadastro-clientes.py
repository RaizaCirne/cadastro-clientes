# Este programa pede ao usuário os dados pessoais de um cliente.
# Armazena os dados na memória RAM e exibe na tela os dados dos clientes cadastrados

from datetime import datetime

nome = input('Digite o nome do cliente: ')

anonasc = int(input('Digite o ano de nascimento: '))
mesnasc = int(input('Digite o mês do nascimento: '))
dianasc = int(input('Digite o dia do nascimento: '))


datanasc = datetime(anonasc, mesnasc, dianasc)
dataatual = datetime.now()
idadecliente = dataatual - datanasc

endereco = input('Digite o endereço: ')
tel = input('Digite o telefone: ')

print('Cliente: {}\nIdade do cliente {}\nTelefone: {}'.format(nome, idadecliente, endereco, tel))
