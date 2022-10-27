# -*- coding: utf-8 -*-
import os
import fitz
import pandas as pd

#selecionando os pdfs
folder = "temp"
def get_files(folder):
    import os
    os.chdir(folder)
    files = os.listdir()
    files = [x for x in files if x.endswith(".pdf")]
    return files 
files = get_files(folder) 
print(files)

#realizando a leitura dos pdfs

doc = fitz.open(folder+'\\'+files[0])
page1 = doc[0]
words = page1.get_text("words")