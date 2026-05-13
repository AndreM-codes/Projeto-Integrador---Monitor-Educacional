import os
import time
from .constructor.introdution_process import introdution_process
from .constructor.censo_escolar_constructor import censo_escolar_constructor

def years(ano_inicial, ano_final):
    return [str(ano) for ano in range(ano_inicial, ano_final + 1)]

def start(cod_municipio, periodo, ConfiguracoesPersonalizadas) -> None:
    while True:
        
        command = introdution_process()

        if command == "1": censo_escolar_constructor(cod_municipio, periodo, ConfiguracoesPersonalizadas)
        else:
            os.system('cls')
            print('\n Comando não encontrado! \n\n')
            time.sleep(1)
            os.system('cls')

