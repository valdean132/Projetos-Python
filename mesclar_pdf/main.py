"""
Mesclador de PDFs

Versão: 1.0
Autor: Valdean Souza
repositório: https://github.com/valdean132/Projetos-Python/mesclar_pdf
"""

import PyPDF2
import os

merger = PyPDF2.PdfMerger() # Criar um objeto PdfMerger

def list_pdfs(pasta):
    list_pdfs = os.listdir(pasta) # Listar todos os arquivos da pasta
    pdfs = [] # Lista para armazenar PDFs encontrados

    if not list_pdfs: # Verifica se a lista de arquivos está vazia
        print('Nenhum Arquivo encontrado.')
        return []

    for pdf in list_pdfs: # Iterar sobre todos os arquivos
        if '.pdf' in pdf: # Verifica se o arquivo é um PDF
            pdfs.append(pdf) # Adicionar PDF à lista

    if not pdfs: # Verifica se a lista de PDFs está vazia
        print('Nenhum PDF encontrado.')
        return []

    pdfs.sort() # Ordenar a lista de PDFs
    return pdfs # Retornar a lista de PDFs encontrados

def merge_pdfs(pdfs, name_new_pdf):
    for pdf in pdfs: # Iterar sobre todos os PDFs
        merger.append(f"pdfs/{pdf}") # Adicionar PDF ao mesclador

    merger.write(f"mesclados/{name_new_pdf}.pdf") # Salvar o PDF mesclado

    print(f'PDFs mesclados com sucesso em mesclados/{name_new_pdf}.pdf') # Mensagem de sucesso
    return # Retornar

def collect_new_name():
    print('Digite o nome do novo PDF (sem .pdf): ') # Solicitar o nome do novo PDF
    while True: # Loop até que um nome válido seja fornecido
        new_name = input('Novo Nome: ') # Solicitar o novo nome
        if new_name.strip(): # Verifica se o nome não está vazio
            new_name = new_name.strip() # Remover espaços em branco
            return new_name # Retornar o novo nome
        else: # Nome inválido
            print('Nome inválido ou campo Vazio. Tente novamente.') # Solicitar um novo nome

if __name__ == "__main__": # Ponto de entrada do programa
    pdfs = list_pdfs('pdfs') # Listar os PDFs na pasta 'pdfs'

    if pdfs:
        name_new_pdf = collect_new_name() # Coletar o nome do novo PDF
        merge_pdfs(pdfs, name_new_pdf) # Mesclar os PDFs encontrados