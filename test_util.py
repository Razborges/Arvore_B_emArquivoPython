# -*- coding: utf-8 -*-

__author__ = 'Rafael Borges'

"""
criado em 12/06/2016
Teste do método de busca na arvore b.
"""

from arvore_b_struct import *
from arvore_b_util import *

try:
    arquivo = open('arvore.dat', 'rb+')
except IOError:
    sys.stderr.write('Arquivo arvore.dat não pode ser aberto para leitura/escrita.')
    sys.exit()

"""TESTE DO MÉTODO DE BUSCA > OK"""
arquivo = open('arvore.dat', 'rb+')
arvore = Arvore()
arquivo.seek(0, 0)
arvore_aux = arvore.le_arvore(arquivo)
#busca_arvore(45, arvore_aux.pagina_raiz, arquivo)
#busca_arvore(11, arvore_aux.pagina_raiz, arquivo)
#busca_arvore(3, arvore_aux.pagina_raiz, arquivo)
#busca_arvore(35, arvore_aux.pagina_raiz, arquivo)
#busca_arvore(66, arvore_aux.pagina_raiz, arquivo)
#busca_arvore(80, arvore_aux.pagina_raiz, arquivo)
#busca_arvore(23, arvore_aux.pagina_raiz, arquivo)

"""TESTE DO MÉTODO IMPRIME EM ORDEM > OK""" 
#imprime_arvore_ordenado(arquivo)

arquivo.close()

"""TESTE DO MÉTODO DE INSERIR >"""
arquivo2 = open('arvore.dat', 'rb+')
chave = Chave(19, 0)
chave2 = Chave(45, 0)
chave3 = Chave(40, 0)
chave4 = Chave(47, 0)
chave5 = Chave(54, 0)
chave6 = Chave(51, 0)
chave7 = Chave(65, 0)
chave8 = Chave(77, 0)
arvore_aux2 = arvore.le_arvore(arquivo2)
pagina_raiz = arvore_aux2.pagina_raiz
insere_arvore(chave2, pagina_raiz, arquivo2)
insere_arvore(chave, pagina_raiz, arquivo2)
insere_arvore(chave3, pagina_raiz, arquivo2)
insere_arvore(chave4, pagina_raiz, arquivo2)
insere_arvore(chave5, pagina_raiz, arquivo2)
insere_arvore(chave6, pagina_raiz, arquivo2)
insere_arvore(chave7, pagina_raiz, arquivo2)
insere_arvore(chave8, pagina_raiz, arquivo2)
busca_arvore(19, arvore_aux2.pagina_raiz, arquivo2)
imprime_arvore_ordenado(arquivo2)

imprime_arvore(arquivo2)

arquivo2.close()