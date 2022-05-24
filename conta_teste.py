from conta import Conta
from random import randint
from historico import Historico
'''Crie um arquivo conta_teste.py e importe a classe conta (from conta import Conta) e realize os seguintes testes.
Crie duas ou mais contas
Realize depósitos, saques e transferências.
Imprima o extrato da conta.'''
sair = False
while not sair:
    opcao = input(
        ('''
---- ESCOLHA UMA OPÇÃO: ----
    [ 1 ] - Criar conta
    [ 2 ] - Depositar
    [ 3 ] - Sacar
    [ 4 ] - Transferir
    [ 5 ] - Ver Extrato
    [S/s] - Sair
        
Qual operação deseja realizar? '''))

    if opcao == '1':  # Criar conta
        titular = str(input('\nNome do titular: ')).upper().strip()
        limite = float(input('\nInforme o valor de limite que deseja: '))
        numero = randint(1000, 9999)
        saldo = 0.0
        transacao = 'Conta Criada com SUCESSO!'
        nova_conta = Conta(numero, titular, saldo, limite, transacao)
        print(nova_conta)

    elif opcao == '2':  # Depositar
        valor = float(
            input('Informe o valor que deseja depositar em sua conta: R$ '))
        if valor < 0:
            print('Você deve informar apenas números!\n\n')
        else:
            nova_conta.deposita(valor)
            print(nova_conta)

    elif opcao == '3':  # Sacar
        valor = float(input('Informe o valor que deseja sacar: R$ '))
        if valor < 0:
            print('Você deve informar apenas números!\n\n')
        else:
            nova_conta.saca(valor)
            print(nova_conta)

    elif opcao == '4':  # Transferir
        valor = float(input('Qual valor deseja transferir? R$ '))
        if valor < 0:
            print('Você deve informar apenas números!\n\n')
        else:
            numConta2 = int(
                input('Qual o número da conta para a qual deseja transferir? '))

            if 9999 > numConta2 < 1000 and numConta2 == nova_conta.numero:
                print('Número da conta inválido. Transação CANCELADA.')
            else:
                nova_conta.transferePara(valor, numConta2)
                print(nova_conta)

    elif opcao == '5':  # Ver extrato
        nova_conta.extrato()
        print(nova_conta)

    elif opcao in 'Ss':
        sair = True
        print('Obrigada, {}! Volte sempre! \n\n'.format(nova_conta.titular))
    else:
        print('Opção inválida.')
