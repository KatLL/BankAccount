''' 
Crie uma classe Histórico (histórico.py) que represente o histórico de uma Conta exibindo a sequência de saldo, saque e depósito. Faça testes no console do Python criando algumas contas, fazendo operações e por último mostrando o histórico de transações de uma Conta.
Crie um arquivo conta_teste.py e importe a classe conta (from conta import Conta) e realize os seguintes testes.
Crie duas ou mais contas
Realize depósitos, saques e transferências.
Imprima o extrato da conta.

EXTRA:
Crie um arquivo data.py quecontencha a class Data.
Esta classe deverá armazenar uma data que contenha, dia, hora, minuto e segundo. 
Modelo uma forma para que cada operação de saque e deposito esteja associado a uma data.'''
from random import randint
from socket import NI_NUMERICHOST
from historico import Historico


class Conta ():
    '''Classe conta bancária com os seguintes atributos e métodos:
  Atributos:
  Número
  Titular
  Saldo
  Limite

  Métodos
  Deposita
  Extrato
  Saca
  TransferePara'''

    def __init__(self, numero, titular, saldo, limite, transacao):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.transacao = transacao
        self.hist = Historico()

    def __str__(self):
        saida = '\n' + ' = '*15 + "\n"
        saida += "Número: " + str(self.numero) + "\n"
        saida += "Titular: " + str(self.titular) + "\n"
        saida += "Saldo: R$ " + str('{:.2f}'.format(self.saldo)) + "\n"
        saida += "Limite: R$ " + str('{:.2f}'.format(self.limite)) + "\n"
        saida += 'Transação: ' + str(self.transacao) + "\n"
        return saida

    def extrato(self):
        '''Extrato (método da classe Histórico)
    Que recebe como argumento uma referência do próprio objeto e imprime o histórico de operações realizados na conta: saques e depósitos.
    '''
        self.numero = self.numero
        self.titular = self.titular
        self.limite = self.limite
        self.saldo = self.saldo
        self.transacao = 'Gerar extrato.'

        dado_conta = [self.numero, self.titular,
                      self.saldo, self.limite, self.transacao]
        self.hist.adicionar(dado_conta)

        ext = self.hist.mostrar()
        print(ext)

    def deposita(self, valor):
        '''Para depositar dinheiro na conta. Esse método deve receber uma referência do próprio objeto e o valor a ser adicionado ao saldo da conta'''
        self.numero = self.numero
        self.titular = self.titular
        self.limite = self.limite
        self.saldo = self.saldo + valor
        self.transacao = 'Depósito de R$ {:.2f}'.format(valor)

        dado_conta = [self.numero, self.titular,
                      self.saldo, self.limite, self.transacao]
        self.hist.adicionar(dado_conta)

    def saca(self, valor):
        '''Que realiza retiradas de dinheiro de uma conta com e retornar um valor que representa se a operação foi ou não bem-sucedida. Lembre-se que não é permitido sacar um valor maior do que o saldo.'''
        self.numero = self.numero
        self.titular = self.titular
        self.limite = self.limite
        self.saldo = self.saldo - valor
        self.transacao = 'Saque de R$ {:.2f}'.format(valor)

        dado_conta = [self.numero, self.titular,
                      self.saldo, self.limite, self.transacao]
        self.hist.adicionar(dado_conta)

    def transferePara(self, valor, numConta2):
        '''Que recebe como argumento uma referência do próprio objeto, uma Conta destino e o valor a ser transferido. Esse método deve sacar o valor do próprio objeto e depositar na conta destino.'''
        self.numero = self.numero
        self.titular = self.titular
        self.limite = self.limite
        self.saldo = self.saldo - valor
        self.transacao = 'Transferência de R$ {:.2f} para a conta {}'.format(
            valor, numConta2)

        dado_conta = [self.numero, self.titular,
                      self.saldo, self.limite, self.transacao]
        self.hist.adicionar(dado_conta)

        titular2 = 'Titular Dois'
        limite2 = 5000.00
        numero2 = numConta2
        saldo2 = 0 + valor
        transacao2 = 'Valor recebido de R$ {:.2f} da conta {}'.format(
            valor, self.numero)
        #conta2 = Conta(numero2, titular2, saldo2, limite2, transacao2)
        print('Dado da conta 2:\n' + str(numero2) + ' ' + str(titular2) +
              ' ' + str(saldo2) + ' ' + str(limite2) + ' ' + str(transacao2) + '\n')
