from elasticsearch import Elasticsearch

# Configuração do Elasticsearch
es = Elasticsearch(['http://localhost:9200/'])

# Nome do índice
index_name = 'k1ppers'

# Apagar o índice
es.indices.delete(index=index_name)
