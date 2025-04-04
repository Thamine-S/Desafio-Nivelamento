import requests
from bs4 import BeautifulSoup
import zipfile
import os

# URL da página que você quer fazer o scraping
url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

# Fazer a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Passar o conteúdo da página para o BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos os links
    links = soup.find_all('a')

    anexos = [link for link in links if 'Anexo' in link.text and link.get('href', '').endswith('.pdf')]

    arquivos_baixados = []
    contador = 1


    for anexo in anexos:
        link_anexo = anexo.get('href')
        if link_anexo:

            if not link_anexo.startswith('http'):
                link_anexo = url + link_anexo 

            nome_arquivo = f'Anexo_{contador}.pdf'  # Nome personalizado

  
            arquivo_response = requests.get(link_anexo)
            if arquivo_response.status_code == 200:
                # Salvar o arquivo localmente
                with open(nome_arquivo, 'wb') as file:
                    file.write(arquivo_response.content)
                print(f'{nome_arquivo} baixado com sucesso!')
                arquivos_baixados.append(nome_arquivo)
                contador += 1 
            else:
                print(f'Falha ao baixar {nome_arquivo}')

    # ZIP
    if arquivos_baixados:
        with zipfile.ZipFile('anexos.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            for arquivo in arquivos_baixados:
                zipf.write(arquivo, os.path.basename(arquivo))  # Adicionar o arquivo ao ZIP
                os.remove(arquivo)  # Remover o arquivo após adicionar ao ZIP

        print("Arquivos compactados em 'anexos.zip' com sucesso!")
else:
    print('Erro na requisição:', response.status_code)
