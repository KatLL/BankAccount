#from conta import Conta

'''Crie um arquivo conta_teste.py e importe a classe conta (from conta import Conta) e realize os seguintes testes.
Crie duas ou mais contas
Realize depósitos, saques e transferências.
Imprima o extrato da conta.'''

opcao = input(
    ('---- ESCOLHA UMA OPÇÃO: ----\n    1 - Criar conta.\n    2 - Depositar.\n    3 - Sacar.\n    4 - Transferir.\n'))

if opcao == '1':
    print('Opção 1')
elif opcao == '2':
    print('Opção 2')
elif opcao == '3':
    print('Opção 3')
elif opcao == '4':
    print('Opção 4')
else:
    print('Número inválido.')
