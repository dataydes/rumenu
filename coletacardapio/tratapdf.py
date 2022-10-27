# -*- coding: utf-8 -*-
import os
import PyPDF2

path = "temp"
os.chdir(path)

def read_text_file(file_path):
    with open(file_path, "r") as f:
        print(f.read())
        pdfFileObj = open(file_path,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        print(pageObj)





for file in os.listdir():
    if file.endswith(".pdf"):
        file_path = f"{path}\{file}"

read_text_file(file_path)

