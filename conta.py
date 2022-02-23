class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero  = numero
        self.__titular = titular
        self.__saldo   = saldo
        self.__limite  = limite

    def extrato(self):
        print("Saldo {} do titular {}". format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, recebedor):
        self.saca(valor)
        recebedor.depositar(valor)

    def get_conta(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_conta(self, numero):
        self.__numero = numero

    def set_titula(self, titular):
        self.__titular = titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_limite(self, limite):
        self.__limite = limite