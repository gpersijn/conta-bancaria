from Aula113.ProjetoBanco.cliente import lista_clientes_poupanca, lista_clientes_corrente
from Aula113.ProjetoBanco.Conta import Conta, Conta_poupanca, Conta_corrente


class Menu:
    def __init__(self, nome, cpf, idade, conta, tipagem):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
        self._conta = conta
        self._tipagem = tipagem

        try:
            if lista_clientes_poupanca[self._conta]['cpf'] == self._cpf:
                self._saldo = lista_clientes_poupanca[self._conta]['saldo']
        except:
            if lista_clientes_corrente[self._conta]['cpf'] == self._cpf:
                self._saldo = lista_clientes_corrente[self._conta]['saldo']

    def tela(self):
        escolha = '0'
        while escolha != 4:
            escolha = int(input('\n1 - Ver dados da conta\n'
                                '2 - Sacar\n'
                                '3 - Depositar \n'
                                '4 - Sair\n'
                                'Escolha: '))
            if escolha == 1:
                self.dados_conta()
                escolha2 = input('\nDesejar retornar ao Menu principal?')
                escolha2 = escolha2.upper()
                if escolha2 not in ['SIM', 'S']:
                    a = 1

            elif escolha == 2:
                valor = float(input('Valor do saque: '))

                if self._tipagem == 'corrente':
                    c = Conta_corrente(self._conta, self._cpf)
                    c.sacar(valor)
                    c.atualizar()

                elif self._tipagem == 'poupanca':
                    c = Conta_poupanca(self._conta, self._saldo)
                    c.sacar(valor)
                    c.atualizar()

            elif escolha == 3:
                valor = float(input('Depósito: '))
                if self._tipagem == 'corrente':
                    c = Conta_corrente(self._conta, self._saldo)
                    c.depositar(valor, self._tipagem)
                    c.atualizar()

                elif self._tipagem == 'poupanca':
                    c = Conta_poupanca(self._conta, self._saldo)
                    c.depositar(valor)
                    c.atualizar()

    def dados_conta(self):
        if self._tipagem == 'poupanca':
            nome = lista_clientes_poupanca[self._conta]['nome']
            cpf = lista_clientes_poupanca[self._conta]['cpf']
            idade = lista_clientes_poupanca[self._conta]['idade']
            saldo = lista_clientes_poupanca[self._conta]['saldo']
        elif self._tipagem == 'corrente':
            nome = lista_clientes_corrente[self._conta]['nome']
            cpf = lista_clientes_corrente[self._conta]['cpf']
            idade = lista_clientes_corrente[self._conta]['idade']
            saldo = lista_clientes_corrente[self._conta]['saldo']

        print(f'\n--------MINHA CONTA---------\n'
              f'Nome - {nome}\n'
              f'Cpf - {cpf}\n'
              f'Idade - {idade}\n'
              f'* Numero da conta - {self._conta}\n'
              f'* Saldo - {saldo}')
