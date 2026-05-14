import os
import subprocess
from src.main.process_handle import start, years
from src.models.censo_escolar_models import Estatisticas

cod_municipio = [
    3543402 # Ribeirão Preto
]

periodo = years(2020,2024) #2020 até 2024

ConfiguracoesPersonalizadas = {  

                        "configuracao_1": Estatisticas(

                                matriculas=["Total"],

                                categorias=['Dependência Administrativa', 
                                            'Escola Privada Conveniada com o Poder Público', 
                                            'Cor/Raça', 'Sexo', 'Faixa Etária','Tempo Integral/Parcial'],
                                
                                etapa=['Educação de Jovens e Adultos - EJA'],

                                niveis={'Educação de Jovens e Adultos - EJA': ['Ensino Fundamental', 
                                                                               'Ensino Médio' ,
                                                                               '(Todos os Valores de Colunas)'],
                                        })
}

if __name__ == "__main__":
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    start(cod_municipio, periodo, ConfiguracoesPersonalizadas)

