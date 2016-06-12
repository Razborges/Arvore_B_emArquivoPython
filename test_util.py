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
busca_arvore(23, arvore_aux.pagina_raiz, arquivo)

arquivo.close()