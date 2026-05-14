import os
import re
from unidecode import unidecode
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from src.models.censo_escolar_models import CensoEscolarModels
from selenium.webdriver.common.by import By



url = CensoEscolarModels.Url
tabela = CensoEscolarModels.Tabela
sem_resultado = CensoEscolarModels.Sem_Resultado

botao = CensoEscolarModels.Botao

class CensoEscolarController:

        def __init__(self) -> None:

                options = Options()
                options.add_argument("--start-minimized")
                options.add_argument("--disable-gpu")  
                options.add_argument('--no-sandbox') 
                options.add_argument("--log-level=3") 
                options.add_argument('--ignore-certificate-errors')

                self.driver = webdriver.Chrome(options=options)        
                self.wait = WebDriverWait(self.driver, 5)
                self.Locais = []


                self.driver.get(url)

        def choose_local(self, cod_municipio, max = 3):
                
                max_attempts = max
                attempt = 1          

                pre_verificacao = self.wait.until(EC.visibility_of_element_located(tabela))
                
                self.__esperar_e_clickar(botao.Selecionar_Membros)
                self.__esperar_e_clickar(botao.SelecMemb.RemoveAll,2)
                
                for _ in range(5):
                        self.driver.switch_to.active_element.send_keys(Keys.TAB)
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                
                self.__esperar_e_clickar(botao.SelecMemb.Pesquisar)
                self.__esperar_e_clickar(botao.Pesq.Capslock_Box)

                select_element = self.driver.find_element(*botao.Pesq.Choise_List)
                select = Select(select_element)
                select.select_by_value('like')
                

                print(' ')

                regiao_anterior = None
                
                for codigo_ibge in cod_municipio:

                        print(codigo_ibge)
                        cidade, regiao = self.__buscar_municipio_por_codigo(codigo_ibge)
                        self.Locais.append(cidade)
                        
                        if regiao == regiao_anterior:
                                text = self.wait.until(EC.visibility_of_element_located(botao.Pesq.Input_Text))
                                text.click()
                                text.send_keys(cidade)
                                text.send_keys(Keys.ENTER)
                                Resultado = (By.XPATH, f'//span[@class="treeNodeDetails"][@title="{cidade}"]')
                                self.wait.until(EC.visibility_of_element_located(Resultado))
                                self.__esperar_e_clickar(botao.SelecMemb.MoveAll, 2)
                                text.send_keys(Keys.CONTROL + 'A')
                                text.send_keys(Keys.BACKSPACE)
                                regiao_anterior = regiao
                        else:
                                self.__esperar_e_clickar(botao.Pesq.Tree_Local)
                                self.__esperar_e_clickar(botao.Tree.Brasil)
                                self.__esperar_e_clickar(botao.Tree.Regiao[regiao])
                                self.__esperar_e_clickar(botao.Tree.Ok)
                                text = self.wait.until(EC.visibility_of_element_located(botao.Pesq.Input_Text))
                                text.click()
                                text.send_keys(cidade)
                                text.send_keys(Keys.ENTER)
                                Resultado = (By.XPATH, f'//span[@class="treeNodeDetails"][@title="{cidade}"]')
                                self.wait.until(EC.visibility_of_element_located(Resultado))
                                self.__esperar_e_clickar(botao.SelecMemb.MoveAll, 2)
                                text.send_keys(Keys.CONTROL + 'A')
                                text.send_keys(Keys.BACKSPACE)
                                regiao_anterior = regiao

                print(' ')
                
                self.__esperar_e_clickar(botao.SelecMemb.Ok)
                wait = WebDriverWait(self.driver, 1)

                while attempt <= max_attempts:        
                        try:    
                                wait.until(EC.visibility_of_element_located(sem_resultado))
                                
                        except:
                                try:
                                        self.__verificacao(pre_verificacao, attempt)
                                        return
                                
                                except:

                                        print(f"O elemento não foi alterado na tentativa {attempt}")
                                        attempt += 1
                                        

        def change_ano(self, ano):

                self.click_input_item(botao.Ano, ano)
                print(ano)

        def change_matricula(self, matricula):
                        
                self.click_input_item(botao.Matricula_Grupo, matricula)

        def change_categoria(self, categoria_1):

                self.click_input_item(botao.Categirias_1, categoria_1)

        def change_etapa(self, etapa):

                self.click_input_item(botao.Etapa_de_Ensino, etapa)

        def change_nivel(self, nivel):

               self.click_input_item(botao.Nivel_de_Ensino, nivel)

        def get_tabela(self, ano, dfs, max = 3):
                
                max_attempts = max
                attempt = 1
                wait = WebDriverWait(self.driver, 1)

                while attempt <= max_attempts:
                       
                        try:    
                                        
                                wait.until(EC.visibility_of_element_located(sem_resultado))
                                return

                        
                        except:

                                try:

                                        element = wait.until(EC.element_to_be_clickable(tabela))
                                        html_content = element.get_attribute("outerHTML")

                                        soup = BeautifulSoup(html_content, 'html.parser')

                                        table = soup.find('table')
                                        
                                        rows = table.find('tbody', recursive=False)
                                        row_cidades = rows.find_all('tr', recursive=False)[2:]

                                        df = pd.read_html(StringIO(str(table)))[0]

                                        df0 = df.loc[0].dropna().tolist()
                                        df3 = df.loc[3].dropna().tolist()

                                        df0.insert(0, df3[0])

                                        itens_a_mover = [item for item in df0 if isinstance(item, str) and item.startswith('Total')]

                                        for item in itens_a_mover:
                                                indice = df0.index(item)
                                                df3.insert(indice, item)

                                        lista_combinada = []

                                        for nome1, nome2 in zip(df0, df3):
                                                nome_completo = nome2 if nome1 == nome2 else nome1 + ' ' + nome2
                                                lista_combinada.append(nome_completo)

                                        rows_listas = []
                                        
                                        for row_cidade in row_cidades:

                                                row_number = [element.text.strip() for element in row_cidade.find_all('td', recursive=False)]
                                                rows_listas.append(self.__transformar_lista(row_number))

                                        self.__verifica_e_adiciona_linha(rows_listas, self.Locais)

                                        rows = []

                                        for row in rows_listas:

                                                df = pd.DataFrame([row])
                                                df.columns = lista_combinada
                                                
                                                df.insert(0, 'Ano', [ano])
                                                df.fillna(0, inplace=True)
                                                
                                                rows.append(df)

                                                print(df)

                                        df_final = pd.concat(rows)
                                        dfs.append(df_final)
                                        
                                        return
                                
                                except Exception as e:

                                        print(f"erro get_tabela na tentativa {attempt}: {e}")
                                        attempt += 1
                
        def click_input_item(self, path, item, max = 3):

                max_attempts = max
                attempt_1 = 1
                attempt_2 = 1

                drop_list = (By.XPATH, f"//div[@class='floatingWindowDiv']//div[@class='masterMenu DropDownValueList']//div[@title='{item}']")                             
                wait = WebDriverWait(self.driver, 1)

                while attempt_2 <= max_attempts:

                        try:
                                pre_verificacao = wait.until(EC.visibility_of_element_located(tabela))

                                while attempt_1 <= max_attempts:
                                        
                                        try:    
                                                
                                                wait.until(EC.visibility_of_element_located(sem_resultado))
                                                print("Sem resultados")
                                                self.__esperar_e_clickar(path)
                                                self.__esperar_e_clickar(drop_list)
                                                time.sleep(1)
                                                return 

                                        except:
                        
                                                
                                                try:

                                                        elemento = wait.until(EC.visibility_of_element_located(path))
                                                        
                                                        title = elemento.get_attribute('title')

                                                        self.__esperar_e_clickar(path)
                                                        self.__esperar_e_clickar(drop_list)

                                                        self.__verificacao(pre_verificacao, attempt_1, item, title)
                                                        return

                                                except:

                                                        print(f"O elemento não foi alterado na tentativa {attempt_1}")
                                                        attempt_1 += 1

                        except:

                                try:
                                        wait.until(EC.visibility_of_element_located(sem_resultado))
                                        print("Sem resultados")
                                        self.__esperar_e_clickar(path)
                                        self.__esperar_e_clickar(drop_list)
                                        time.sleep(1)
                                        return

                                except: 
                                        attempt_2 += 1               

        def __esperar_e_clickar(self, path, attempt=1):

                button = self.wait.until(EC.visibility_of_element_located(path))
                for _ in range(attempt):
                        button.click()

        def __verificacao(self, pre_verificacao, attempt, item = "sem", title = "item"):
                
                wait = WebDriverWait(self.driver, 1)

                if attempt == 1 and title == item:
                        print('opção atual escolhida')
                else:
                        wait.until(EC.staleness_of(pre_verificacao))
                        print(f"opção atualizada")
 
        def __transformar_lista(self, lista):
                nova_lista = []
                for elemento in lista:
                        if elemento.replace('.', '').isdigit():
                                nova_lista.append(int(elemento.replace('.', '')))
                        else:
                                nova_lista.append(elemento if elemento.strip() != '' else 0)
                return nova_lista
        
        def __verifica_e_adiciona_linha(self, lista_de_listas, lista_de_nomes):

                nomes_faltando = [nome for nome in lista_de_nomes if nome not in [item[0] for item in lista_de_listas]]

                if nomes_faltando:
                        nova_linha = [0] * len(lista_de_listas[0])  
                        
                        for nome in nomes_faltando:

                                nova_linha[0] = nome
                                lista_de_listas.append(nova_linha.copy())

                return lista_de_listas
        
        def __buscar_municipio_por_codigo(self, cod):

                url = f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{cod}"
                try:
                        response = requests.get(url)
                        response.raise_for_status()
                        municipio = response.json()
                        
                        nome = municipio['nome']
                        regiao = municipio['microrregiao']['mesorregiao']['UF']['regiao']['nome']

                        return nome, regiao
                
                except requests.RequestException as e:
                        print(f"Erro ao acessar a API do IBGE: {e}")
                        return exit()
                except KeyError:
                        print("Código IBGE inválido ou informações não encontradas.")
                        return exit()

class SinopseEscolarController:

    def sinopse_concat(diretorio: str, codigos_cidades: list[int], paginas_contem: None|str, nome_arquivo_saida):
        
        # Lista e ordena os arquivos
        arquivos = sorted([
            nome_arquivo for nome_arquivo in os.listdir(diretorio)
            if nome_arquivo.startswith('Sinopse_Estatistica_da_Educação_Basica') 
            and nome_arquivo.endswith('.xlsx')
        ])

        planilhas_filtradas = {}
        renomes_paginas = {}
        ultimo_ano = ''

        for nome_arquivo in arquivos:
            ano = re.search(r'\d{4}', nome_arquivo).group()
            if nome_arquivo == arquivos[-1]:
                ultimo_ano = f'-{ano[-2:]}'
            
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            xl = pd.ExcelFile(caminho_arquivo)
            paginas = xl.sheet_names
            
            if paginas_contem:
                
                df = xl.parse('Sumário')
                col_zero = df.columns[0]
                linhas_com_eja = df[df[col_zero].astype(str).str.contains(paginas_contem, na=False)][col_zero].str.split().str[0].tolist()
                paginas = [item for item in paginas if any(term in item for term in linhas_com_eja)]
            
                
        
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
    
                    if not codigos_cidades:
                        
                        df['Ano'] = int(ano)
                        df['Código do Município'] = pd.to_numeric(df['Código do Município'], errors='coerce')
                        linhas_cidades = df.dropna(subset=['Código do Município'])
                                            
                        if titulo in planilhas_filtradas:
                            planilhas_filtradas[titulo] = pd.concat([planilhas_filtradas[titulo], linhas_cidades])
                        else:
                            planilhas_filtradas[titulo] = linhas_cidades
                    
                    else:
                        for codigo_cidade in codigos_cidades:
                            df['Ano'] = int(ano)
                            linhas_cidades = df[df['Código do Município'] == codigo_cidade]
                            
                            if titulo in planilhas_filtradas:
                                planilhas_filtradas[titulo] = pd.concat([planilhas_filtradas[titulo], linhas_cidades])
                            else:
                                planilhas_filtradas[titulo] = linhas_cidades

        # Salvar resultados em um arquivo Excel
        SinopseEscolarController.salvar_resultados(planilhas_filtradas, renomes_paginas, nome_arquivo_saida, ultimo_ano)

    def ajustar_dataframe(df, df_referencia):
        if len(df.columns) < len(df_referencia.columns):
            for _ in range(len(df_referencia.columns) - len(df.columns)):
                df[f'new_column_{len(df.columns)}'] = None
        elif len(df.columns) > len(df_referencia.columns):
            df = df.iloc[:, :len(df_referencia.columns)]
        
        df.columns = df_referencia.columns
        return df

    def criar_dataframe(df):
        index_regiao = df[df['Voltar ao Sumário'].str.startswith('Região', na=False)]
        index_brasil = df[df['Voltar ao Sumário'].str.startswith('Brasil', na=False)]
        
        primeira_linha = df.iloc[index_regiao.index].index[0]
        ultima_linha = df.iloc[index_brasil.index - 1].index[0]
        linhas_entre = df.iloc[primeira_linha:ultima_linha]

        df_preenchido_y = linhas_entre.ffill(axis=0)
        df_preenchido_xy = df_preenchido_y[2:].ffill(axis=1)
        
        linhas_listas = df_preenchido_xy.values.tolist()
        linhas_processadas = SinopseEscolarController.processar_lista_de_listas(linhas_listas)
        
        cabeçalho = SinopseEscolarController.gerar_cabecalho(linhas_processadas)
        cabeçalho[0] = 'Ano'  # Renomeia a primeira coluna
        
        df.columns = cabeçalho
        return pd.DataFrame(columns=cabeçalho)

    def processar_lista_de_listas(lista_de_listas):
        penultima_linha = len(lista_de_listas) - 2
        lista_processada = []

        for i, lista in enumerate(lista_de_listas):
            nova_lista = []
            iterator = iter(lista)
            primeiro_total = True

            for item in iterator:
                if item.startswith('Total') and i == penultima_linha:
                    if primeiro_total:
                        primeiro_total = False
                        nova_lista.append(item)
                    else:
                        proximo_item = next(iterator, '')
                        nova_lista.extend([proximo_item, proximo_item])
                else:
                    nova_lista.append(item)

            lista_processada.append(nova_lista)

        return lista_processada


    def gerar_cabecalho(linhas):
        cabeçalho = []
        for coluna in range(len(linhas[-1])):
            valores = [linhas[i][coluna] for i in range(len(linhas))]
            valores = [re.sub(r'(?<=[A-Za-z])\d.*$', '', v).strip() for v in valores]  # Remove números e traços grudados a letras
            valores_unicos = list(dict.fromkeys(valores))
            cabeçalho.append(' '.join(valores_unicos))
        return cabeçalho

    def salvar_resultados(planilhas_filtradas, renomes_paginas, nome_arquivo_saida, ultimo_ano):
        with pd.ExcelWriter(nome_arquivo_saida) as writer:
            for titulo, linhas_filtradas in planilhas_filtradas.items():
                linhas_filtradas.to_excel(writer, 
                                        sheet_name=renomes_paginas[titulo].replace(ultimo_ano, ''), 
                                        index=False)