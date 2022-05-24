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

    def __init__ (self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.hist= Historico()


    def __str__(self):
        saida  = "Número:" + str(self.numero) + "\n"
        saida += "Saldo" + str(self.saldo) + "\n"
        return saida



    def extrato(self):
        '''Extrato (método da classe Histórico)
    Que recebe como argumento uma referência do próprio objeto e imprime o histórico de operações realizados na conta: saques e depósitos.
    '''
        print(self.hist.mostrar())

    def deposita(self, valor):
        '''Para depositar dinheiro na conta. Esse método deve receber uma referência do próprio objeto e o valor a ser adicionado ao saldo da conta'''
        self.numero = self.numero
        self.titular = self.titular
        self.limite = self.limite
        self.saldo = self.saldo + valor

        dado_conta = [self.numero, self.titular, self.saldo, self.limite]
        self.hist.adicionar(dado_conta)


    def saca(self, valor):
        '''Que realiza retiradas de dinheiro de uma conta com e retornar um valor que representa se a operação foi ou não bem-sucedida. Lembre-se que não é permitido sacar um valor maior do que o saldo.'''
        self.numero = self.numero
        self.titular = self.titular
        self.limite = self.limite
        self.saldo = self.saldo - valor

        dado_conta = [self.numero, self.titular, self.saldo, self.limite]
        self.hist.adicionar(dado_conta)

        
    def transferePara(self):
        '''Que recebe como argumento uma referência do próprio objeto, uma Conta destino e o valor a ser transferido. Esse método deve sacar o valor do próprio objeto e depositar na conta destino.'''
        pass