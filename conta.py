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

    def pode_sacar(self, valor):
        valor_disponivel = self.__limite + self.__saldo
        return valor <= valor_disponivel


    def saca(self, valor):

        if(self.pode_sacar() == True):
            self.__saldo -= valor
        else:
            print("Valor Solicitado: {} \n Valor Disponível: {} \n Valor indisponível".format(valor, (self.__saldo+self.__limite)))

    def transferir(self, valor, recebedor):
        self.saca(valor)
        recebedor.depositar(valor)

    @property
    def conta(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @conta.setter
    def conta(self, numero):
        self.__numero = numero

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite