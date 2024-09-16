class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos
        self.titular = titular  # Nome do titular da conta (público)
        self.__saldo = saldo_inicial  # Saldo da conta (privado)