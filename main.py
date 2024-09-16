class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        # Atributos
        self.titular = titular  # Nome do titular da conta (público)
        self.__saldo = saldo_inicial  # Saldo da conta (privado)

    # Método para depositar dinheiro na conta (público)
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo atual: R${self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    # Método para sacar dinheiro da conta (público)
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.__saldo}")
        else:
            print("Saque inválido ou saldo insuficiente.")

    # Método para consultar o saldo (público)
    def consultar_saldo(self):
        return self.__saldo

# Exemplo de herança - Conta Poupança herda de ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo_inicial=0, taxa_juros=0.01):
        # Chamada ao construtor da classe base (ContaBancaria)
        super().__init__(titular, saldo_inicial)
        self.taxa_juros = taxa_juros  # Taxa de juros específica para Conta Poupança

    # Polimorfismo - Sobrescrevendo o método da classe base
    def aplicar_juros(self):
        juros = self.consultar_saldo() * self.taxa_juros
        self.depositar(juros)
        print(f"Juros de R${juros} aplicados. Saldo atual: R${self.consultar_saldo()}")


# Polimorfismo: Função que pode receber diferentes tipos de contas
def exibir_detalhes_conta(conta):
    print(f"Titular: {conta.titular}")
    print(f"Saldo atual: R${conta.consultar_saldo()}")


# Exemplo de uso
conta_simples = ContaBancaria("Carlos", 1000)
conta_simples.depositar(500)
conta_simples.sacar(200)
exibir_detalhes_conta(conta_simples)

conta_poupanca = ContaPoupanca("Maria", 2000)
conta_poupanca.aplicar_juros()  # Aplicando juros
exibir_detalhes_conta(conta_poupanca)
