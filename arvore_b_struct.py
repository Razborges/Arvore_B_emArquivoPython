# -*- coding: utf-8 -*-

__author__ = 'Rafael Borges'

"""
criado em 06/06/2016
Definição das estruturas da arvore b: Arvore, Pagina e Chave
"""

import struct
from operator import attrgetter

MAX_CHAVES = 5 #CONSTANTE para definir o número máximo de chaves por página

class Arvore(object):
    """Definiçõs das características da Arvore"""
    def __init__(self, qtd_chaves_pagina = MAX_CHAVES):
        self._qtd_chaves_pagina = int(qtd_chaves_pagina)
        self._pagina_raiz = int(0)

    @property
    def qtd_chaves_pagina(self):
        return self._qtd_chaves_pagina

    @property
    def pagina_raiz(self):
        return self._pagina_raiz

    def set_pagina_raiz(self, pagina_raiz):
        self._pagina_raiz = int(pagina_raiz)

    def escreve_arvore(self, file):
        arvore_binaria = struct.pack('qq', self._qtd_chaves_pagina, self._pagina_raiz)
        file.write(arvore_binaria)

    def le_arvore(self, file):
        line = file.read(struct.calcsize('qq'))
        aux = struct.unpack('qq', line)
        arvore = Arvore(aux[0])
        arvore.set_pagina_raiz(aux[1])
        return arvore

class Pagina(object):
    """Define a estrutura de cada página da arvore B que contém as chaves"""
    def __init__(self):
        self._qtd_chaves = int(0)
        self._chaves = []
        self._pos_pagina_maior_chave = int(0)
        self._ponteiro_pai = int(0)

    @property
    def qtd_chaves(self):
        return self._qtd_chaves

    def set_qtd_chaves(self, qtd):
        self._qtd_chaves = qtd

    @property
    def chaves(self):
        return self._chaves

    def inclui_chave(self, chave):
        self._chaves.append(chave)
        self._qtd_chaves += 1
        self._chaves.sort(key=attrgetter("chave"))

    @property
    def pos_pagina_maior_chave(self):
        return self._pos_pagina_maior_chave

    def set_pos_pagina_maior_chave(self, posicao):
        self._pos_pagina_maior_chave = int(posicao)

    @property
    def ponteiro_pai(self):
        return self._ponteiro_pai

    def set_ponteiro_pai(self, ponteiro):
        self._ponteiro_pai = ponteiro

    def escreve_pagina(self, file):
        qtd_chaves_binario = struct.pack('q', self._qtd_chaves)
        file.write(qtd_chaves_binario)
        for j in range(0, MAX_CHAVES):
            if (j + 1) <= self._qtd_chaves:
                chave_binaria = struct.pack('qqq', self._chaves[j].chave, self._chaves[j].ponteiro_arquivo,
                                self._chaves[j].pos_pagina_menor_chave)
                file.write(chave_binaria)
            else:
                zero = struct.pack('qqq', 0, 0, 0)
                file.write(zero)
        pos_maior_binario = struct.pack('q', self._pos_pagina_maior_chave)
        file.write(pos_maior_binario)
        ponteiro_pai_binario = struct.pack('q', self._ponteiro_pai)
        file.write(ponteiro_pai_binario)

    def le_pagina(self, file):
        pagina = Pagina()
        qtd_chaves_binario = file.read(struct.calcsize('q'))
        qtd_chaves = struct.unpack('q', qtd_chaves_binario)
        pagina.set_qtd_chaves(qtd_chaves[0])
        for j in range(0, pagina.qtd_chaves):
            chave_binaria = file.read(struct.calcsize('qqq'))
            chave_aux = struct.unpack('qqq', chave_binaria)
            chave = Chave(chave_aux[0], chave_aux[1], chave_aux[2])
            pagina.chaves.append(chave)
            pagina.chaves.sort(key=attrgetter("chave"))
        for i in range(pagina.qtd_chaves, MAX_CHAVES):
            zero = file.read(struct.calcsize('qqq'))
        pos_maior_binario = file.read(struct.calcsize('q'))
        pos_maior = struct.unpack('q', pos_maior_binario)
        pagina.set_pos_pagina_maior_chave(pos_maior[0])
        ponteiro_pai_binario = file.read(struct.calcsize('q'))
        ponteiro_pai = struct.unpack('q', ponteiro_pai_binario)
        pagina.set_ponteiro_pai(ponteiro_pai[0])
        return pagina

class Chave(object):
    """Define as propriedade da chave"""

    def __init__(self, chave, ponteiro, pos_pagina_menor_chave = 0):
        self._chave = int(chave)
        self._ponteiro_arquivo = int(ponteiro)
        self._pos_pagina_menor_chave = int(pos_pagina_menor_chave)

    @property
    def chave(self):
        return self._chave

    @property
    def ponteiro_arquivo(self):
        return self._ponteiro_arquivo

    @property
    def pos_pagina_menor_chave(self):
        return self._pos_pagina_menor_chave

    def set_pos_pagina_menor_chave(self, posicao):
        self._pos_pagina_menor_chave = int(posicao)