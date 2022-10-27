# -*- coding: utf-8 -*-
from ast import Try
import os
import camelot

#selecionando os pdfs
folder = "temp"
def get_files(folder):
    import os
    os.chdir(folder)
    files = os.listdir()
    files = [x for x in files if x.endswith(".pdf")]
    return files 

#realizando a leitura dos pdfs
def readPDF(arqpdf):
    tables = camelot.read_pdf(arqpdf)
    print (tables[0].df)


files = get_files(folder) 
print(files)
print(os.getcwd())
arq0 = readPDF(files[0])