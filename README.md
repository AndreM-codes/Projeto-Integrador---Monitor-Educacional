# Projeto Integrador de Simplificação de Dados do INEP

Este projeto é uma ferramenta que permite concatenar, simplificar e apresentar arquivos extraidos do Inep para o Monitoramento Municipal Educacional. É ideal para quem precisa otimizar esses arquivos de forma rápida e eficiente. 

## Funcionalidades

- **Web scraping Oracle BI INEP**: Filtra as cidades pelo seu código IBGE.
- **Concatenação e Simplificação de Arquivos das Sinopses do INEP**: Junta todos os anos de cada arquivo.
- **Apresentação facilitada de dados para Web via Shiny**: Melhora o layout das tabelas.

## Resultados

### Web scraping Censo Escolar

![alt text](<doc/imgs/Captura 3.png>)

### Sinopses do INEP
#### Antes

![alt text](<doc/imgs/Captura 1.png>)

#### Depois

![alt text](<doc/imgs/Captura 2.png>)

## Como Usar

**Clone o repositório** ou apenas baixe o .ipynb (para isso, você precisará das sinopses disponíveis nos canais de Dados Abertos do INEP).

**Use o script**:

```bash
command.py
```

![alt text](<doc/imgs/Captura 4.png>)

**Mude as variáveis, caso necessário**: Altere as variáveis para modificar a lista de cidades procuradas.

**Resultados**: O script irá gerar os arquivos na pasta `file`.

## Bibliotecas Utilizadas

- `pandas`: Para manipulação e análise de dados.
- `unidecode`: Para normalização de textos, removendo acentos e caracteres especiais.
- `selenium`: Para automação de navegação e interação com páginas web.
- `requests`: Para realização de requisições HTTP.
- `beautifulsoup4`: Para extração e parsing de informações em HTML/XML.
- `openpyxl`: Para leitura, edição e criação de arquivos Excel (`.xlsx`).
- `lxml`: Para processamento eficiente de XML e HTML.