from elasticsearch import Elasticsearch, helpers
import hashlib
import threading
import re
import os

# Configuração do Elasticsearch
es = Elasticsearch(['http://localhost:9200/'], timeout=30, max_retries=10, retry_on_timeout=True)

index_name = 'k1ppers'

# Lock para sincronizar o acesso aos contadores
lock = threading.Lock()

def create_index_action(line, counters):
    global lock
    
    cleaned_line = line.strip()
    # Dividir a linha usando um delimitador específico que sabemos que não aparece na URL
    parts = re.split(';|\\|', cleaned_line, maxsplit=2)
    
    if len(parts) == 3:
        url, username, password = parts
        # Agora não precisamos nos preocupar em dividir a URL incorretamente
        document = {
            "url": url,
            "username": username,
            "password": password
        }
        doc_hash = hashlib.sha256((url + username + password).encode()).hexdigest()

        if not es.exists(index=index_name, id=doc_hash):
            action = {
                "_op_type": "index",
                "_index": index_name,
                "_id": doc_hash,
                "_source": document
            }
            with lock:
                counters['added_counter'] += 1
            return action
        else:
            with lock:
                counters['duplicate_counter'] += 1
    else:
        with lock:
            counters['invalid_counter'] += 1
        print(f"Linha considerada inválida: {cleaned_line}")
    return None

def process_file(file_path, counters):
    batch = []
    try:
        with open(file_path, 'r', encoding='utf-8') as txtfile:
            for i, line in enumerate(txtfile):
                action = create_index_action(line, counters)
                if action:
                    batch.append(action)
                
                if len(batch) >= 1000:
                    helpers.bulk(es, batch)
                    batch.clear()
                    print(f"Processado lote de 1000 documentos até agora.")

            if batch:
                helpers.bulk(es, batch)
                print("Processado último lote de documentos.")
    except Exception as e:
        print(f"Erro ao processar arquivo {file_path}: {e}")

def main(directory_path):
    counters = {'added_counter': 0, 'duplicate_counter': 0, 'invalid_counter': 0}
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            print(f"Processando o arquivo: {filename}")
            process_file(file_path, counters)
    print(f"Processamento concluído. Linhas adicionadas: {counters['added_counter']}, Duplicatas: {counters['duplicate_counter']}, Inválidas: {counters['invalid_counter']}")

if __name__ == "__main__":
    main('C:/Users/vicktor/Downloads/CLOUD')  # Substitua pelo diretório de destino
