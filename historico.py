from dataHora import DataHora


class Historico ():
    ''' classe para registrar o histórico de transações. classe Histórico (histórico.py) que represente o histórico de uma Conta exibindo a sequência de saldo, saque e depósito.'''

    def __init__(self):
        self.historico = []

    def mostrar(self):
        tamanho = len(self.historico)
        hist = self.historico.split()

        for c in range(tamanho + 1):
            saida = '\n' + ' = ' * 15 + "\n"
            saida += "Número: " + str(hist[0][0]) + "\n"
            saida += "Titular: " + str(hist[0][1]) + "\n"
            saida += "Saldo: R$ " + str('{:.2f}'.format(hist[0][2])) + "\n"
            saida += "Limite: R$ " + str('{:.2f}'.format(hist[0][3])) + "\n"
            saida += 'Transação: ' + str(hist[0][4]) + "\n"
            saida += 'Data e Hora: ' + str(hist[0][5]) + "\n"
            print(saida)
            c += 1

    def adicionar(self, dado_conta):
        data = DataHora()

        registro = [dado_conta, data]

        self.historico.append(registro)
