from BankAccount.dataHora import DataHora
#from conta import Conta


class Historico ():
    ''' classe para registrar o histórico de transações. classe Histórico (histórico.py) que represente o histórico de uma Conta exibindo a sequência de saldo, saque e depósito.'''

    def __init__(self):
        self.historico = []

    def mostrar(self):
        pass

    def adicionar(self, dado_conta):
        data = DataHora()

        registro = [dado_conta, data]

        self.histortico.append(registro)