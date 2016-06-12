# -*- coding: utf-8 -*-

__author__ = 'Rafael Borges'

"""
criado em 12/06/2016
Definição dos métodos de busca, inserção e remoção na arvore b.
"""
from arvore_b_struct import *
import sys

def busca_arvore(key, ponteiro, arquivo):
    pagina = Pagina()
    arquivo.seek(ponteiro)
    pagina_aux = pagina.le_pagina(arquivo)
    for i in range(0, pagina_aux.qtd_chaves):
        if key == pagina_aux.chaves[i].chave:
            print("\nChave " + str(pagina_aux.chaves[i].chave) + " já se encontra na árvore.\n")
            sys.exit()
    for i in range(0, pagina_aux.qtd_chaves):
        if key < pagina_aux.chaves[i].chave:
            if pagina_aux.chaves[i].pos_pagina_menor_chave == 0:
                print("\nChave " + str(key) + " não encontrada nesta árvore.\n")
                sys.exit()
            else:
                busca_arvore(key, pagina_aux.chaves[i].pos_pagina_menor_chave, arquivo)
    busca_arvore(key, pagina_aux.pos_pagina_maior_chave, arquivo)

def insere_arvore(chave, ponteiro, pagina_pai, arquivo):
    busca_arvore(chave.chave, ponteiro, arquivo)
    pass

def remove_arvore(chave, ponteiro, arquivo):
    pass

def imprime_arvore_ordenado(arquivo):
    pass