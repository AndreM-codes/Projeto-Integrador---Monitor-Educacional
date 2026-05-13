# Projeto .ipynb: Concatenação e Simplificação de Arquivos das Sinopses do INEP

Este projeto é uma ferramenta que permite concatenar e simplificar todos os arquivos da Sinopse Básica de uma pasta. É ideal para quem precisa otimizar esses arquivos de forma rápida e eficiente.

## Funcionalidades

- **Filtragens**: Filtra as cidades pelo seu código IBGE.
- **Concatenação**: Junta todos os anos de cada arquivo.
- **Simplificação**: Melhora o layout das tabelas.

## Resultados

### Antes

![alt text](<doc/imgs/Captura 1.png>)

### Depois

![alt text](<doc/imgs/Captura 2.png>)

## Como Usar

**Clone o repositório** ou apenas baixe o .ipynb (para isso, você precisará das sinopses disponíveis nos canais de Dados Abertos do INEP).

**Abra o script**:
```bash
Sinopse_Basica_Concat.ipynb
```

**Mude as variáveis, caso necessário**: Altere as variáveis para modificar a lista de cidades procuradas.

**Resultados**: O script irá gerar um novo arquivo concatenado e simplificado.

## Bibliotecas Utilizadas

- `os`: Para manipulação de diretórios e arquivos.
- `re`: Para operações com expressões regulares.
- `unidecode`: Para normalizar textos, removendo acentos.
- `pandas`: Para manipulação e análise de dados.
