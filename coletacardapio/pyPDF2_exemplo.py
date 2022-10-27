# -*- coding: utf-8 -*-
import os
import PyPDF2

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
    pdfFileObj = open(arqpdf,'rb')
    pdfRead = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfRead.getPage(1)
    return print(pageObj.extractText())

files = get_files(folder) 
print(files)
arq0 = readPDF(files[0])