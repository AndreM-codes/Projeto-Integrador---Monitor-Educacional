import os
import subprocess
import re
import time
import pandas as pd
from unidecode import unidecode
from src.view.censo_escolar_view import Censo_Escolar_View
from src.models.censo_escolar_models import Estatisticas
from src.controllers.censo_escolar_controller import CensoEscolarController, SinopseEscolarController

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

                case "9":
                        Configuracoes = None
                        subprocess.run('cls', shell=True)

        if Configuracoes:
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

def sinopse_escolar_constructor(Cidades, Anos, command):
        diretorio = "file/Inep Data/Sinopses Estatísticas Censo Escolar"
        nome_arquivo_saida = 'file/Inep Data/Sinopse_Estatistica_Concat_Edu_Basica.xlsx'

        # Lista e ordena os arquivos
        arquivos = sorted([
            nome_arquivo for nome_arquivo in os.listdir(diretorio)
            if nome_arquivo.startswith('Sinopse_Estatistica_da_Educação_Basica')
               and any(nome_arquivo.endswith(f"{ano}.xlsx") for ano in Anos)
        ])

        planilhas_filtradas = {}
        renomes_paginas = {}
        ultimo_ano = ''

        if not arquivos:
              subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
              print(f'\n Nenhum arquivo de Sinopses encontrado na Pasta:\n{diretorio}/\n\n')
              input("Voltar: ENTER")
              subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        else:
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            for nome_arquivo in arquivos:
                ano = re.search(r'\d{4}', nome_arquivo).group()
                if nome_arquivo == arquivos[-1]:
                        ultimo_ano = f'-{ano[-2:]}'

                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                xl = pd.ExcelFile(caminho_arquivo)
                paginas = xl.sheet_names

                if command:
                    df = xl.parse('Sumário')
                    col_zero = df.columns[0]
                    linhas_filtrada = df[df[col_zero].astype(str).str.contains(re.escape(command), na=False)][col_zero].str.split().str[0].tolist()
                    paginas = [item for item in paginas if any(term in item for term in linhas_filtrada)]



                for nome_pagina in paginas:
                    df = xl.parse(nome_pagina)
                    print(f'{nome_arquivo}: {nome_pagina}')

                    if df.empty:
                        continue

                    if df.columns[0] == 'Voltar ao Sumário':
                        titulo = unidecode(df['Voltar ao Sumário'].iloc[2])
                        substituicoes = {
                                ', por Etapa de Ensino': ', por Ano',
                                ' Regular': '',
                                '–': '-',
                                '.': '',
                            }

                        for chave, valor in substituicoes.items():
                            titulo = titulo.replace(chave, valor)

                        titulo = re.sub(r'^\d+\s-\s+', '', titulo)
                        titulo = re.sub(r'\s+-\s\d+$', '', titulo)
                        palavras = re.findall(r'[A-Z]\w+', titulo)
                        titulo = ' '.join(palavras)

                            # Processamento do DataFrame
                        if titulo in planilhas_filtradas:
                            renomes_paginas[titulo] = f'{nome_pagina}-{ano[-2:]}'
                            df = SinopseEscolarController.ajustar_dataframe(df, planilhas_filtradas[titulo])
                        else:
                            renomes_paginas[titulo] = f'{nome_pagina}-{ano[-2:]}'

                            df = SinopseEscolarController.criar_dataframe(df)

                        if not Cidades:
                            df['Ano'] = int(ano)
                            df['Código do Município'] = pd.to_numeric(df['Código do Município'], errors='coerce')
                            linhas_cidades = df.dropna(subset=['Código do Município'])

                            if titulo in planilhas_filtradas:
                                planilhas_filtradas[titulo] = pd.concat([planilhas_filtradas[titulo], linhas_cidades])
                            else:
                                planilhas_filtradas[titulo] = linhas_cidades

                        else:
                            for codigo_cidade in Cidades:
                                df['Ano'] = int(ano)
                                linhas_cidades = df[df['Código do Município'] == codigo_cidade]

                                if titulo in planilhas_filtradas:
                                    planilhas_filtradas[titulo] = pd.concat([planilhas_filtradas[titulo], linhas_cidades])
                                else:
                                    planilhas_filtradas[titulo] = linhas_cidades

            # Salvar resultados em um arquivo Excel
            if planilhas_filtradas:
                SinopseEscolarController.salvar_resultados(planilhas_filtradas, renomes_paginas, nome_arquivo_saida, ultimo_ano)
            else:
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
                print(f'\n Nenhuma Planilha encontrada com o Filtro:\n{command}\n\n')
                input("Voltar: ENTER")
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

