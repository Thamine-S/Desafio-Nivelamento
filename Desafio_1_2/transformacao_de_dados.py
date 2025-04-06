import zipfile
import pdfplumber
import csv
import time
import shutil
import os
import pandas as pd

# Caminho para o arquivo ZIP
zip_file_path = 'anexos.zip'
extract_folder = 'C:\\Users\\Usuario\\Desktop\\Importante\\projetos\\Desafio_1_2\\anexos'
diretorio = 'C:\\Users\\Usuario\\Desktop\\Importante\\projetos\\Desafio_1_2'
arquivos_baixados = []

# Descompactar o arquivo ZIP
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

# Supondo que o PDF está dentro do ZIP
pdf_file_path = os.path.join(extract_folder, 'anexo_1.pdf')

# Abrir o PDF usando pdfplumber
with pdfplumber.open(pdf_file_path) as pdf:
    todas_as_tabelas = []
    
    for page_num in range(2, 181):  
        page = pdf.pages[page_num]
        
        # Extrair a tabela da página
        table = page.extract_table()
        
        if table:
            todas_as_tabelas.extend(table)  # Acumula as tabelas extraídas de cada página
        else:
            print(f'Nenhuma tabela encontrada na página {page_num + 1}.')  # Exibe uma mensagem se não encontrar tabela

# Verificar se foi possível extrair alguma tabela
if todas_as_tabelas:
    # Caminho para o arquivo CSV de saída
    csv_file_path = os.path.join(extract_folder, 'tabela.csv')

    # Salvar todas as tabelas extraídas em um arquivo CSV
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in todas_as_tabelas:
            writer.writerow(row)

    arquivos_baixados.append(csv_file_path)
    print(f'Dados salvos em {csv_file_path}')
else:
    print('Não foi possível extrair nenhuma tabela de 3 a 181.')
    
time.sleep(10)

csv = "anexos\\tabela.csv"

df = pd.read_csv(csv, encoding="utf-8", header=0)

header_values = df.columns.tolist()  # Obtém os nomes reais das colunas

# Converter todas as colunas para string e remover espaços extras
df_str = df.astype(str).apply(lambda x: x.str.strip())

# Filtrar as linhas que são exatamente iguais ao cabeçalho (exceto a primeira ocorrência)
mask = (df_str == header_values).all(axis=1)

# Remover todas as repetições do cabeçalho, preservando apenas a linha original
df_clean = df[~mask]

df_clean.rename(columns={"RN\n(alteração)":"RN(alteração)","OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)

# Salvar o arquivo limpo
df_clean.to_csv("tabela_limpa.csv", index=False, encoding="utf-8")

print("Arquivo processado com sucesso! As repetições do cabeçalho foram removidas.")

# Caminho do arquivo CSV que foi processado
arquivo_origem = "tabela_limpa.csv"

# Novo diretório para onde o arquivo será movido
novo_diretorio = "C:\\Users\\Usuario\\Desktop\\Importante\\projetos\\Desafio_1_2\\anexos"

# Criar o caminho completo do arquivo no novo diretório
arquivo_destino = f"{novo_diretorio}\\tabela_limpa.csv"

# Mover o arquivo
shutil.move(arquivo_origem, arquivo_destino)

print(f"Arquivo movido para {arquivo_destino} com sucesso!")


# Compactar o arquivo CSV em um novo arquivo ZIP
if arquivos_baixados:
    with zipfile.ZipFile('Teste_thamine.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos_baixados:
            zipf.write(arquivo, os.path.basename(arquivo))  # Adicionar o arquivo ao ZIP
    shutil.rmtree(extract_folder)

    print("Arquivos compactados em 'Teste_thamine.zip' com sucesso!")

