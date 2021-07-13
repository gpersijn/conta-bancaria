def validador_cpf(cpf: str):
    try:
        verificacao = False
        cpf = cpf.replace('.', '')
        lista_um, lista_dois = cpf[:9], cpf[-2:]
        x = 1
        y = 10
        digito = a = 0

        while x == 1:
            soma = 0

            for var in lista_um:
                soma += int(var) * y
                y -= 1
            soma += int(digito) * 2

            confirme = 11 - (soma % 11)

            if confirme > 9:
                digito = str('0')
            else:
                digito = str(confirme)

            if str(confirme) == lista_dois[1] and a > 0:
                verificacao = True
                break
            if digito != lista_dois[0] or len(lista_um) * lista_um[0] == lista_um:
                verificacao = False
                x += 1

            y = 11
            a += 1

        return verificacao
    except:
        return False

