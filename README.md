# Demos do Elasticsearch em Python

Este repositório contém exemplos de scripts em Python para interagir com o Elasticsearch. Você encontrará demos para visualizar linhas, pesquisar e indexar arquivos em um nó do Elasticsearch. Estes scripts são úteis para quem está aprendendo a utilizar o Elasticsearch ou precisa de exemplos práticos para integrar o Elasticsearch em seus projetos Python.

## Pré-requisitos

Para executar os scripts deste repositório, você precisará:

- Python 3.6 ou superior
- Elasticsearch 7.x ou superior
- Biblioteca `elasticsearch` para Python

## Instalação

Primeiro, instale as dependências necessárias usando `pip`:

```bash
pip install elasticsearch
pip install requests
``` 

## Execução 
`python indexar.py` 
- Serve para indexar seus arquivos dentro do seu nó.<br>**Não esqueça de trocar o código de acordo com suas fucionalidades** 

`python apagar_indice.py` 
- Serve para apagar um indíce dentro do elastic.<br>**Verifique o nome do índice dentro do código**

`python pesquisar.py` 
- Serve para pesquisar palavras dentro do seu nó.<br>

  `python ver_indices.py` 
- Serve para ver os indices dentro do seu nó.<br>
