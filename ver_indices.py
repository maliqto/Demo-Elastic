from elasticsearch import Elasticsearch

# Configuração do Elasticsearch
es = Elasticsearch(['http://localhost:9200/'])

# Obter a lista de todos os índices
all_indices = es.indices.get_alias(index="*")

# Imprimir a lista de índices
for index in all_indices:
    print(index)
