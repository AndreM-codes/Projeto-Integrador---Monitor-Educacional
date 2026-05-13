import os
from typing import Dict

class Censo_Escolar_View:
    def escolha_local(self):
        os.system('cls||clear')

        print(

'''
        InepData Censo Escolar  
              
Capitar Censo Escolar Completo - 1
Capitar Censo Escolar Personalizado - 2

'''

)

        command = input('Iniciar:  ')

        return command
