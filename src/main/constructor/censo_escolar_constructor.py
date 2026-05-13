import os
import pandas as pd
from src.view.censo_escolar_view import Censo_Escolar_View
from src.models.censo_escolar_models import Estatisticas
from src.controllers.censo_escolar_controller import CensoEscolarController

ConfiguracoesCompletas = {
     
                        "configuracao_1": Estatisticas(

                                matriculas=["Total", "Educação Especial", "Classes Comuns", "Classes Exclusivas"],
                                categorias=['Faixa Etária', 'Dependência Administrativa', 'Escola Privada Conveniada com o Poder Público','Cor/Raça', 'Sexo', 'Tempo Integral/Parcial'],
                                etapa=['Educação Básica'],
                                niveis={'Educação Básica': ['Educação Básica']}

                        ),
                        "configuracao_2": Estatisticas(

                                matriculas=["Total"],
                                categorias=['Dependência Administrativa', 'Escola Privada Conveniada com o Poder Público', 'Cor/Raça', 'Sexo', 'Faixa Etária','Tempo Integral/Parcial'],
                                etapa=['Educação Infantil', 'Ensino Fundamental', 'Ensino Médio', 'Educação Profissional', 'Educação de Jovens e Adultos - EJA'],
                                niveis={'Educação Infantil': ['Creche', 'Pré-escola','(Todos os Valores de Colunas)'],
                                        'Ensino Fundamental': ['Anos Iniciais', 'Anos Finais','(Todos os Valores de Colunas)'],
                                        'Ensino Médio': ['Propedêutico','Curso Técnico Integrado','(Todos os Valores de Colunas)'],
                                        'Educação Profissional': ['Técnica', 'Não Técnica','(Todos os Valores de Colunas)'],
                                        'Educação de Jovens e Adultos - EJA': ['Ensino Fundamental', 'Ensino Médio' ,'(Todos os Valores de Colunas)'],
                                        })

                }
                
siglas_matriculas = {
                        'Total' : '',
                        'Educação Especial' : '(EE) ',
                        'Classes Comuns': '(CC) ',
                        'Classes Exclusivas': '(CE) '

                }

siglas_categorias = {

                        'Categoria Administrativa': 'Adm',
                        'Dependência Administrativa': 'Dep', 
                        'Tempo Integral/Parcial': 'Integral e Parcial', 
                        'Escola Privada Conveniada com o Poder Público': 'Escolas Conveniadas', 
                        'Sexo': 'Sexo',
                        'Cor/Raça': 'Cor', 
                        'Faixa Etária': 'Faixa Etária'

                }
                
siglas_ensinos = {
                        'Educação Básica': '',
                        'Educação Infantil': 'Inf',
                        'Ensino Fundamental': 'EF',
                        'Ensino Médio': 'EM',
                        'Educação Profissional': 'EP',
                        'Educação de Jovens e Adultos - EJA': 'EJA'                      
                }

sigla_niveis =  {        
                        '(Todos os Valores de Colunas)': "",
                        'Educação Básica': ' Bas',
                        'Educação Infantil': ' Inf',
                        'Educação Profissional': ' EP',
                        'Educação de Jovens e Adultos - EJA': ' EJA',                  
                        'Creche':' Cre', 
                        'Pré-escola':' Pre',
                        'Anos Iniciais':' AI',
                        'Anos Finais':' AF',
                        'Propedêutico':' Prop',
                        'Curso Técnico Integrado':' CTI',
                        'Técnica':'T', 
                        'Não Técnica':'nT',
                        'Ensino Fundamental':' EF',
                        'Ensino Médio':' EM'
     
} 

def censo_escolar_constructor(Cidades, Anos, ConfiguracoesPersonalizadas):

        inep_view = Censo_Escolar_View()

        censo_escolar_controller = CensoEscolarController()
        command = inep_view.escolha_local()

        match command:

                case "1":
                        Configuracoes = ConfiguracoesCompletas
                              
                case "2":
                        Configuracoes = ConfiguracoesPersonalizadas

        censo_escolar_controller.choose_local(Cidades)

        for configuracao in Configuracoes:

                configuracao_atual = Configuracoes[configuracao]

                Matriculas = configuracao_atual.matriculas
                Categorias = configuracao_atual.categorias
                Etapas = configuracao_atual.etapa
                Niveis_ = configuracao_atual.niveis

                for matricula in Matriculas:

                        print(matricula)
                        sigla_matricula = siglas_matriculas[matricula]
                        censo_escolar_controller.change_matricula(matricula)

                        for categoria in Categorias:

                                print(categoria)
                                sigla_categoria = siglas_categorias[categoria]
                                censo_escolar_controller.change_categoria(categoria)


                                for etapa in Etapas:

                                        print(etapa)
                                        sigla_ensino = siglas_ensinos[etapa]
                                        censo_escolar_controller.change_etapa(etapa)
                                        Niveis = Niveis_[etapa]

                                        for nivel in Niveis:
                                        
                                                print(nivel)
                                                sigla_nivel = sigla_niveis[nivel]
                                                dir = 'file/Inep Data/Estatísticas Censo Escolar'
                                                os.makedirs(dir, exist_ok=True)
                                                nome_arquivo = f'{sigla_matricula}{sigla_ensino}{sigla_nivel} - {sigla_categoria}.csv'

                                                censo_escolar_controller.change_nivel(nivel)
                                                dfs = []

                                                for ano in Anos:
                                                
                                                        censo_escolar_controller.change_ano(ano)
                                                        censo_escolar_controller.get_tabela(ano, dfs)
                                                        try:
                                                                result = pd.concat(dfs, axis=0, ignore_index=True, sort=False)
                                                                result.fillna(0, inplace=True)
                                                                print(result)

                                                                pasta = os.path.join(dir)
                                                                result.to_csv(f"{pasta}/{nome_arquivo}",encoding="utf-8-sig", sep=";",index=False)
                                                        except:
                                                                pass               

    
