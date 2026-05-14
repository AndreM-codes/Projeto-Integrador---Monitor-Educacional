import os
import subprocess
import time
from .constructor.introdution_process import introdution_process
from .constructor.censo_escolar_constructor import censo_escolar_constructor, sinopse_escolar_constructor

def years(ano_inicial, ano_final):
    return [str(ano) for ano in range(ano_inicial, ano_final + 1)]

def start(cod_municipio, periodo, ConfiguracoesPersonalizadas) -> None:
    while True:
        
        command = introdution_process()
        
        match command:
        
            case "1": 
                censo_escolar_constructor(cod_municipio, periodo, ConfiguracoesPersonalizadas)

            case "2":
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                print('\n Filtrar por Palavra-Chave no Título?\nSim - 1\nSem Filtrar - ENTER\nVoltar - 9\n\n')
                command = input('Comando:  ')
                if command != "9":
                    command = input('\n\Palavra-Chave:  ')
                    sinopse_escolar_constructor(cod_municipio, periodo, command)
                else:
                    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            
            case "9":
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                return
            
            case _:
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                print('\n Comando não encontrado! \n\n')
                time.sleep(1)
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

