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
from socket import NI_NUMERICHOST


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

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self):
        '''Para depositar dinheiro na conta. Esse método deve receber uma referência do próprio objeto e o valor a ser adicionado ao saldo da conta'''
        pass

    def extrato(self):
        '''Extrato (método da classe Histórico)
    Que recebe como argumento uma referência do próprio objeto e imprime o histórico de operações realizados na conta: saques e depósitos.
    '''
        pass

    def saca(self):
        '''Que realiza retiradas de dinheiro de uma conta com e retornar um valor que representa se a operação foi ou não bem-sucedida. Lembre-se que não é permitido sacar um valor maior do que o saldo.'''
        pass

    def transferePara(self):
        '''Que recebe como argumento uma referência do próprio objeto, uma Conta destino e o valor a ser transferido. Esse método deve sacar o valor do próprio objeto e depositar na conta destino.'''
        pass
