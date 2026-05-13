from selenium.webdriver.common.by import By


class CensoEscolarModels:
    Url = "https://anonymousdata.inep.gov.br/analytics/saw.dll?Portal&PortalPath=%2Fshared%2FDissemina%C3%A7%C3%A3o%20dos%20Censos%2FEduca%C3%A7%C3%A3o%20B%C3%A1sica%2FPain%C3%A9is%2FCenso%20da%20Educa%C3%A7%C3%A3o%20B%C3%A1sica&Page=Matr%C3%ADcula%20-%20Por%20Ano"
    Selecionar_Membros = (By.XPATH, "//img[@title='Selecionar Membros']")
    Tabela = (By.XPATH, "/html/body/div[8]/table[1]/tbody/tr[1]/td[2]/div/table[1]/tbody/tr/td[2]/div[1]/div/table[3]/tbody/tr/td[1]/div/table/tbody/tr[2]/td/div/div[3]/table/tbody/tr/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/div/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/div[2]/table/tbody/tr[3]/td/table")   
    Sem_Resultado = (By.XPATH, "//h2[@class='alert_h'][text()='Sem resultado']")
                        
    class Botao:
        Ano = (By.XPATH, "//input[starts-with(@id, 'saw_') and substring(@id, string-length(@id) - string-length('_4_1') + 1) = '_4_1']")                     
        Selecionar_Membros = (By.XPATH, "//img[@title='Selecionar Membros']")     
        Etapa_de_Ensino  = (By.XPATH, "//input[starts-with(@id, 'saw_') and substring(@id, string-length(@id) - string-length('_6_1') + 1) = '_6_1']")     
        Nivel_de_Ensino  = (By.XPATH, "//input[starts-with(@id, 'saw_') and substring(@id, string-length(@id) - string-length('_7_1') + 1) = '_7_1']")
        Matricula_Grupo = (By.XPATH, "//input[starts-with(@id, 'saw_') and substring(@id, string-length(@id) - string-length('_9_1') + 1) = '_9_1']")
        Categirias_1 = (By.XPATH, "//input[starts-with(@id, 'saw_') and substring(@id, string-length(@id) - string-length('_a_1') + 1) = '_a_1']")
        Categirias_2 = (By.XPATH, "//input[starts-with(@id, 'saw_') and substring(@id, string-length(@id) - string-length('_b_1') + 1) = '_b_1']")

        class SelecMemb:
            Pesquisar = (By.XPATH, "//input[@id='choiceListSearchString_D']")
            RemoveAll = (By.CSS_SELECTOR, "#idRemoveAllButton")
            MoveAll = (By.CSS_SELECTOR, "#idMoveAllButton")
            Ok = (By.XPATH, "(//a[@name='OK'])[1]")

        class Pesq:
            Input_Text = (By.XPATH, "//input[@id='choiceListSearchString_D']")
            Choise_List = (By.XPATH, "//select[@id='choiceListSearch_op']")
            Capslock_Box = (By.XPATH, "//input[@id='matchCase']")
            Tree_Local = (By.XPATH, "//img[@id='AvailableDataBrowserGroupBoxTreeButton']")

        class Tree:
            Brasil = (By.XPATH, "//img[@id='whyNeedAnID$LocalidadeDim.LocalidadeDim_SearchMemberSelect$Brasil_Brasil_disclosure']")
            Regiao = {
                'Centro-Oeste': (By.CSS_SELECTOR, '#whyNeedAnID\$LocalidadeDim\.LocalidadeDim_SearchMemberSelect\$Regi\%c3\%a3o_Centro-Oeste_details > span'),
                'Nordeste': (By.CSS_SELECTOR, '#whyNeedAnID\$LocalidadeDim\.LocalidadeDim_SearchMemberSelect\$Regi\%c3\%a3o_Nordeste_details > span'),
                'Norte': (By.CSS_SELECTOR, '#whyNeedAnID\$LocalidadeDim\.LocalidadeDim_SearchMemberSelect\$Regi\%c3\%a3o_Norte_details > span'),
                'Sudeste': (By.CSS_SELECTOR, '#whyNeedAnID\$LocalidadeDim\.LocalidadeDim_SearchMemberSelect\$Regi\%c3\%a3o_Sudeste_details > span'),
                'Sul': (By.CSS_SELECTOR, '#whyNeedAnID\$LocalidadeDim\.LocalidadeDim_SearchMemberSelect\$Regi\%c3\%a3o_Sul_details > span'),
                }
            Ok = (By.XPATH, "(//a[@name='OK'])[2]")

        class Estatisticas:

            def __init__(self, matriculas, categorias, etapa, niveis):
                self.matriculas = matriculas
                self.categorias = categorias
                self.etapa = etapa
                self.niveis = niveis

class Estatisticas:
    def __init__(self, matriculas, categorias, etapa, niveis):        
        self.matriculas = matriculas
        self.categorias = categorias
        self.etapa = etapa
        self.niveis = niveis

  


















