import os
import subprocess

class Censo_Escolar_View:
    def escolha_local(self):
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

        print(

'''
        InepData Censo Escolar  
              
Capitar Censo Escolar Completo - 1
Capitar Censo Escolar Personalizado - 2
Voltar - 9

'''

)

        command = input('Iniciar:  ')

        return command
