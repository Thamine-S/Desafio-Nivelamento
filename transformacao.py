import pandas as pd
import csv
import os
import shutil

# Lista de arquivos CSV
arquivos = ['temp/1T2023.csv', 'temp/1T2024.csv', 'temp/2T2023.csv', 'temp/2T2024.csv', 
            'temp/3T2023.csv', 'temp/3T2024.csv', 'temp/4T2023.csv', 'temp/4T2024.csv']

# Processando os arquivos
def processar_arquivo(arquivo):
    try:
        # Tenta detectar o delimitador automaticamente
        df = pd.read_csv(arquivo, sep=None, engine='python', dtype=str)

        # Modificar apenas as colunas específicas
        colunas_modificar = ['VL_SALDO_INICIAL', 'VL_SALDO_FINAL']
        for col in colunas_modificar:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

        # Salvar o arquivo modificado
        df.to_csv(arquivo, index=False, quotechar='"')
        print(f"Arquivo processado e salvo: {arquivo}")
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")

for arquivo in arquivos:
    processar_arquivo(arquivo)
    


def wrap_csv_values(input_files: list, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    
    for input_file in input_files:
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        
        with open(input_file, newline='', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            
            for row in reader:
                writer.writerow(row)
        
        print(f"Arquivo processado e salvo como {output_file}")

# Exemplo de uso
input_csv_files = ["temp/1T2023.csv", "temp/1T2024.csv", "temp/2T2023.csv", "temp/2T2024.csv", "temp/3T2023.csv", "temp/3T2024.csv", "temp/4T2023.csv", "temp/4T2024.csv"]  # Substitua pelos nomes dos seus arquivos
output_directory = "C:\\Users\\Usuario\\Desktop\\Importante\\projetos\\Intuitive Care\\data"  # Pasta onde os arquivos serão salvos
wrap_csv_values(input_csv_files, output_directory)

shutil.rmtree('C:\\Users\\Usuario\\Desktop\\Importante\\projetos\\Intuitive Care\\temp', ignore_errors=True)
