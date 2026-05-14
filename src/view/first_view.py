def introduction_page():

    message = """

        Banco de Dados Educacionais

Obter dados do Painel Oracle Inep - 1
Limpar dados da Sinopse do Censo Escolar - 2
Sair - 9

"""

    print(message)

    command = input('Comando:  ')

    return command