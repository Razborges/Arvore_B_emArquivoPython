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
        return
    for i in range(0, pagina_aux.qtd_chaves):
        if key < pagina_aux.chaves[i].chave:
            if pagina_aux.chaves[i].pos_pagina_menor_chave == 0:
                print("\nChave " + str(key) + " não encontrada nesta árvore.\n")
            else:
                busca_arvore(key, pagina_aux.chaves[i].pos_pagina_menor_chave, arquivo)
            return
    busca_arvore(key, pagina_aux.pos_pagina_maior_chave, arquivo)

def insere_arvore(chave, ponteiro, arquivo):
    pagina = Pagina()
    arquivo.seek(ponteiro)
    pagina_aux = pagina.le_pagina(arquivo)
    for i in range(0, pagina_aux.qtd_chaves):
        if chave.chave == pagina_aux.chaves[i].chave:
            print('Chave já está na árvore.')
            return
        if chave.chave < pagina_aux.chaves[i].chave:
            if pagina_aux.chaves[i].pos_pagina_menor_chave == 0:
                pagina_aux.inclui_chave(chave)
                if pagina_aux.qtd_chaves < MAX_CHAVES:
                    arquivo.seek(ponteiro)
                    pagina_aux.escreve_pagina(arquivo)
                    print('Chave inserida na árvore com sucesso.')
                    return
                else:
                    split(pagina_aux, ponteiro, arquivo)
                    return
            else:
                ponteiro = pagina_aux.chaves[i].pos_pagina_menor_chave
                insere_arvore(chave, ponteiro, arquivo)
                return
    if chave.chave > pagina_aux.chaves[pagina_aux.qtd_chaves - 1].chave:
        if pagina_aux.pos_pagina_maior_chave == 0:
            pagina_aux.inclui_chave(chave)
            if pagina_aux.qtd_chaves < MAX_CHAVES:
                    arquivo.seek(ponteiro)
                    pagina_aux.escreve_pagina(arquivo)
                    print('Chave inserida na árvore com sucesso.')
            else:
                split(pagina_aux, ponteiro, arquivo)
        else:
            ponteiro = pagina_aux.pos_pagina_maior_chave
            insere_arvore(chave, ponteiro, arquivo)

def split(pagina, ponteiro, arquivo):
    chave_aux = Chave(0, 0)
    pagina_aux1 = Pagina()
    pagina_aux2 = Pagina()
    pagina_aux3 = Pagina()
    for i in range(0, pagina.qtd_chaves):
        if i < (MAX_CHAVES)//2:
            pagina_aux2.inclui_chave(pagina.chaves[i])
        if i == (MAX_CHAVES)//2:
            chave_aux = pagina.chaves[i]
        if i > (MAX_CHAVES)//2:
            pagina_aux3.inclui_chave(pagina.chaves[i])
    pos = arquivo.seek(ponteiro)
    chave_aux.set_pos_pagina_menor_chave(pos)
    pagina_aux2.set_ponteiro_pai(pagina.ponteiro_pai)
    pagina_aux2.escreve_pagina(arquivo)
    arquivo.seek(0, 2)
    pagina_aux3.set_ponteiro_pai(pagina.ponteiro_pai)
    pagina_aux3.escreve_pagina(arquivo)
    arquivo.seek(pagina.ponteiro_pai)
    pagina_aux1 = pagina_aux1.le_pagina(arquivo)
    pagina_aux1.inclui_chave(chave_aux)
    if pagina_aux1.qtd_chaves == MAX_CHAVES:
        split(pagina_aux1, pagina.ponteiro_pai, arquivo)
    else:
        arquivo.seek(pagina.ponteiro_pai)
        pagina_aux1.escreve_pagina(arquivo)
        print('Chave inserida na árvore com sucesso.')

def remove_arvore(chave, ponteiro, arquivo):
    pass

def imprime_arvore_ordenado(arquivo):
    arvore = Arvore()
    arquivo.seek(0, 0)
    limitador = arquivo.tell()
    lista = []
    arvore_aux = arvore.le_arvore(arquivo)
    print('Esta arvore b possui número máximo de chaves: ' + str(arvore_aux.qtd_chaves_pagina))
    pagina = Pagina()
    tamanho_arquivo = arquivo.seek(0, 2)
    arquivo.seek(arvore_aux.pagina_raiz)
    while limitador < tamanho_arquivo:
        pagina_aux = pagina.le_pagina(arquivo)
        for i in range(0, pagina_aux.qtd_chaves):
            lista.append(pagina_aux.chaves[i])
        limitador = arquivo.tell()
    lista.sort(key=attrgetter("chave"))
    for chave in lista:
        print(chave.chave, end=' ')

def imprime_arvore(arquivo):
    arquivo.seek(0, 0)
    arvore_aux = Arvore()
    arvore_aux = arvore_aux.le_arvore(arquivo)
    pagina = Pagina()
    limitador = arquivo.seek(0, 2)
    arquivo.seek(arvore_aux.pagina_raiz)
    while pagina:
        aux = arquivo.tell()
        if aux == limitador:
            break
        pagina_aux = pagina.le_pagina(arquivo)
        print('\nPOSICAO NO ARQUIVO: ' + str(aux))
        print("Quantidades de chaves nesta página: " + str(pagina_aux.qtd_chaves))
        print("Pagina Pai: " + str(pagina_aux.ponteiro_pai))
        for i in range(0, int(pagina_aux.qtd_chaves)):
            print("Chave: " + str(pagina_aux.chaves[i].chave) + " - " + str(pagina_aux.chaves[i].pos_pagina_menor_chave))