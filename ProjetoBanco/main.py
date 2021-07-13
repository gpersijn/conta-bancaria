from Aula113.ProjetoBanco.cliente import Clientes, lista_clientes_corrente, lista_clientes_poupanca
from Aula113.ProjetoBanco.ValidadorDeCPF import validador_cpf
from Aula113.ProjetoBanco.menu_banco import Menu


print('--------BANCO---------')
cpf = input('Digite seu cpf: ')

while not validador_cpf(cpf):
    print('Digite um cpf válido.')
    cpf = input('Digite seu cpf: ')
    print()

p = Clientes()
tipagem = p.verifique_cadastro(cpf)

if tipagem == 'corrente' or tipagem == 'poupanca':
    a = 0
    while a == 0:
        senha = input('Digite sua senha: ')
        if p.verifique_senha(senha, tipagem):
            a = 1
            p = Menu(p.nome, p.cpf, p.idade, p.conta, tipagem)
            p.tela()
        else:
            print('Senha inválida\n')


else:
    resposta = input('Verificamos que o CPF digitado ainda não possui uma conta bancária. Gostaria de criar um conta?')
    resposta = resposta.lower()
    if resposta in ['sim', 's']:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        senha = input('Digite sua nova senha para esse CPF: ')
        if idade >= 18:
            p = Clientes(nome, idade, cpf)
            p.cadastre(senha)
            p = Menu(p.nome, p.cpf, p.idade, p.conta)
            p.tela()
        else:
            print('Voce nao possui idade suficiente para ser cadastrado')

