import csv
import json

def tsv_to_json(tsv_file, json_file):
    # Lê o arquivo TSV
    with open(tsv_file, 'r', encoding='utf-8') as tsv:
        reader = csv.DictReader(tsv, delimiter='\t')
        data = []

        for row in reader:
            # Cria um dicionário separado para cada elemento
            separated_row = {key: value for key, value in row.items()}
            data.append(separated_row)

    # Escreve os dados no arquivo JSON
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        json.dump(data, jsonf, indent=4)

# Exemplo de uso
tsv_file = 'dados.tsv'  # Substitua pelo seu arquivo TSV
json_file = 'dados.json'  # Nome do arquivo JSON de saída

tsv_to_json(tsv_file, json_file)