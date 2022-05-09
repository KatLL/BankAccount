from datetime import datetime


class DataHora ():
    '''Classe para estabelecer data e hora da operação.
    Crie um arquivo data.py quecontencha a class Data.
Esta classe deverá armazenar uma data que contenha, dia, hora, minuto e segundo. 
Modelo uma forma para que cada operação de saque e deposito esteja associado a uma data.'''

    def __init__(self):
        self.data_hora = []

    def adicionar_data_hora(self):
        data_atual = datetime.now()
        data_atual_formatada = data_atual.strftime('%d/%m/%Y %H:%M')

        self.data_hora.append(data_atual_formatada)
