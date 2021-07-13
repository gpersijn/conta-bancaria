from abc import ABC, abstractmethod
from Aula113.ProjetoBanco.cliente import lista_clientes_poupanca, lista_clientes_corrente


class Conta(ABC):
    def __init__(self, conta, saldo):
        self._conta = conta
        self._saldo = saldo

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @abstractmethod
    def sacar(self, valor): pass

    def depositar(self, valor, tipagem):
        if tipagem == 'poupanca':
            self._saldo = lista_clientes_poupanca[self._conta]['saldo']
            self._saldo += valor
        elif tipagem == 'corrente':
            self._saldo = lista_clientes_corrente[self._conta]['saldo']
            self._saldo += valor

    def verifique_conta(self):
        if self._conta in lista_clientes_poupanca:
            return 'poupanca'
        if self._conta in lista_clientes_corrente:
            return 'corrente'


class Conta_poupanca(Conta):
    def __init__(self, conta, saldo):
        super().__init__(conta, saldo)

    def sacar(self, valor):
        self._saldo = lista_clientes_poupanca[self._conta]['saldo']
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print('Saldo insuficiente para este saque.')

    def atualizar(self):
        lista_clientes_poupanca[self._conta]['saldo'] = self._saldo
        print(self._saldo)
        print(lista_clientes_poupanca)


class Conta_corrente(Conta):
    def __init__(self, conta, saldo):
        super().__init__(conta, saldo)
        self._limite = 100

    def sacar(self, valor):
        self._saldo = lista_clientes_corrente[self._conta]['saldo']
        if self._saldo + self._limite >= valor:
            self._saldo = self.saldo - valor
        else:
            print('Saldo insuficiente para este saque.')

    def atualizar(self):
        lista_clientes_corrente[self._conta]['saldo'] = self._saldo
        print(self._saldo)
        print(lista_clientes_corrente)

