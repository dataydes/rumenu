# -*- coding: utf-8 -*-
import fitz
conteudo = ""
with fitz.open("cardapio.pdf") as pdf:
    for pagina in pdf:
        conteudo += pagina.getText()
conteudo