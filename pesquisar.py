from elasticsearch import Elasticsearch

# Configuração do Elasticsearch
es = Elasticsearch(['http://localhost:9200/'])

# Nome do índice
index_name = 'k1ppers'

# Consulta de busca
query = {
    "query": {
        "match": {
            "url": "seguidores"
        }
    }
}

# Fazer a busca
response = es.search(index=index_name, body=query)

# Imprimir o número total de hits (documentos retornados)
print(f"Número total de documentos retornados: {response['hits']['total']['value']}")

# Imprimir a resposta
for hit in response['hits']['hits']:
    print(f"Documento ID: {hit['_id']}, Pontuação: {hit['_score']}, Documento: {hit['_source']}")
