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

dias = idadecliente.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30

endereco = input('Digite o endereço: ')
tel = input('Digite o telefone: ')

print('Cliente: {}\nIdade do cliente: {} anos\nEnderaço: {}\nTelefone: {}'.format(nome, anos, endereco, tel))
