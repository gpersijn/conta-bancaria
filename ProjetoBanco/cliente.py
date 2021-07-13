from random import randint

lista_clientes_poupanca = {
    '123456-P': {'senha': 'graviola',
                 'nome': 'Gustave',
                 'idade': 19,
                 'cpf': '41825538379',
                 'saldo': 100}
}
lista_clientes_corrente = {
    '654321-C': {'senha': 'melancia',
                 'nome': 'Elisane',
                 'idade': 76,
                 'cpf': '74151166076',
                 'saldo': 0}
}


class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._saldo = None

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def cpf(self):
        return self._cpf


class Clientes(Pessoa):
    def __init__(self, nome=None, idade=None, cpf=None):
        super().__init__(nome, idade, cpf)
        self._conta = None
        self._senha = None

    @property
    def conta(self):
        return self._conta

    @property
    def senha(self):
        return self.senha

    @staticmethod
    def verifique_cadastro(cpf_dado):
        for key, value in lista_clientes_poupanca.items():
            if cpf_dado == value['cpf']:
                tipagem = 'poupanca'
                return tipagem

        for key2, value2 in lista_clientes_corrente.items():
            if cpf_dado == value2['cpf']:
                tipagem = 'corrente'
                return tipagem

    def verifique_senha(self, senha_dada, tipagem):
        if tipagem == 'poupanca':
            for key, value in lista_clientes_poupanca.items():
                if senha_dada == value['senha']:
                    self._senha = value['senha']
                    self._nome = value['nome']
                    self._idade = value['idade']
                    self._cpf = value['cpf']
                    self._saldo = value['saldo']
                    self._conta = key
                    return True
        elif tipagem == 'corrente':
            for key, value in lista_clientes_corrente.items():
                if senha_dada == value['senha']:
                    self._senha = value['senha']
                    self._nome = value['nome']
                    self._idade = value['idade']
                    self._cpf = value['cpf']
                    self._saldo = value['saldo']
                    self._conta = key
                    return True

    def cadastre(self, senha):

        escolha = int(input('\n1 - Conta Poupança\n'
                            '2 - Conta Corrente\n'
                            'Escolha o tipo de conta que vc deseja ter: \n'))
        if escolha == 1:
            self._conta = str(randint(100000, 999999)) + '-P'
            self._senha = senha
            atributos = ['senha', 'nome', 'idade', 'cpf', 'saldo']
            dados = [self._senha, self._nome, self._idade, self._cpf, 0]
            lista_clientes_poupanca[self._conta] = dict(zip(atributos, dados))

        if escolha == 2:
            self._conta = str(randint(100000, 999999)) + '-C'
            self._senha = senha
            atributos = ['senha', 'nome', 'idade', 'cpf', 'saldo']
            dados = [self._senha, self._nome, self._idade, self._cpf, 0]
            lista_clientes_corrente[self._conta] = dict(zip(atributos, dados))



# def verifique_conta(self):
#     if  in lista_clientes_poupanca:
#         return 'poupanca'
#     if conta in lista_clientes_corrente:
#         return 'corrente'
