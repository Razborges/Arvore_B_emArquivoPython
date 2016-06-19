# -*- coding: utf-8 -*-

__author__ = 'Rafael Borges'

"""
criado em 12/06/2016
Teste da escrita e leitura da árvore, página e chave.
"""

from arvore_b_struct import *

try:
    arquivo = open('arvore.dat', 'wb+')
except IOError:
    sys.stderr.write('Arquivo arvore.dat não pode ser aberto para leitura/escrita.')
    sys.exit()

"""TESTANDO A ORDENAÇÃO DAS CHAVES > OK"""
"""chave1 = Chave(1, 1)
chave2 = Chave(2, 2)
chave3 = Chave(3, 3)

pagina = Pagina()
pagina.inclui_chave(chave2)
pagina.inclui_chave(chave3)
pagina.inclui_chave(chave1)
print(pagina.qtd_chaves)
for chave in pagina.chaves:
	print(chave.chave)
"""
"""TESTANDO SE ESTAVA ESCREVENDO A ARVORE > OK"""
arvore = Arvore()
arquivo.seek(0, 0)
arvore.escreve_arvore(arquivo)

pagina_raiz = Pagina()
pagina1 = Pagina()
pagina2 = Pagina()
pagina3 = Pagina()
pagina4 = Pagina()
pagina5 = Pagina()
pagina6 = Pagina()
pagina7 = Pagina()
pagina8 = Pagina()
pagina9 = Pagina()

chave45 = Chave(45, 45)
chave11 = Chave(11, 11)
chave20 = Chave(20, 20)
chave30 = Chave(30, 30)
chave56 = Chave(56, 56)
chave80 = Chave(80, 80)
chave3 = Chave(3, 3)
chave5 = Chave(5, 5)
chave7 = Chave(7, 7)
chave14 = Chave(14, 14)
chave18 = Chave(18, 18)
chave22 = Chave(22, 22)
chave25 = Chave(25, 25)
chave28 = Chave(28, 28)
chave33 = Chave(33, 33)
chave35 = Chave(35, 35)
chave38 = Chave(38, 38)
chave42 = Chave(42, 42)
chave50 = Chave(50, 50)
chave53 = Chave(53, 53)
chave60 = Chave(60, 60)
chave66 = Chave(66, 66)
chave72 = Chave(72, 72)
chave82 = Chave(82, 82)
chave94 = Chave(94, 94)

pagina_raiz.inclui_chave(chave45)
pagina1.inclui_chave(chave11)
pagina1.inclui_chave(chave20)
pagina1.inclui_chave(chave30)

pagina2.inclui_chave(chave56)
pagina2.inclui_chave(chave80)

pagina3.inclui_chave(chave3)
pagina3.inclui_chave(chave5)
pagina3.inclui_chave(chave7)

pagina4.inclui_chave(chave14)
pagina4.inclui_chave(chave18)

pagina5.inclui_chave(chave22)
pagina5.inclui_chave(chave25)
pagina5.inclui_chave(chave28)

pagina6.inclui_chave(chave33)
pagina6.inclui_chave(chave35)
pagina6.inclui_chave(chave38)
pagina6.inclui_chave(chave42)

pagina7.inclui_chave(chave50)
pagina7.inclui_chave(chave53)

pagina8.inclui_chave(chave60)
pagina8.inclui_chave(chave66)
pagina8.inclui_chave(chave72)

pagina9.inclui_chave(chave82)
pagina9.inclui_chave(chave94)

"""TESTANDO SE ESTÁ LENDO A ARVORE E ESCREVENDO AS PAGINAS > OK"""
arquivo.seek(0, 0)
arvore_aux = arvore.le_arvore(arquivo)
arvore_aux.set_pagina_raiz(arquivo.seek(0, 2))
arquivo.seek(0,0)
arvore_aux.escreve_arvore(arquivo)
pagina_raiz.escreve_pagina(arquivo)
arquivo.seek(arvore_aux.pagina_raiz)
pagina_raiz = pagina_raiz.le_pagina(arquivo)
pagina_raiz.chaves[0].set_pos_pagina_menor_chave(arquivo.seek(0, 2))
pagina1.set_ponteiro_pai(arvore_aux.pagina_raiz)
pagina1.escreve_pagina(arquivo)
pagina_raiz.set_pos_pagina_maior_chave(arquivo.seek(0, 2))
pagina2.set_ponteiro_pai(arvore_aux.pagina_raiz)
pagina2.escreve_pagina(arquivo)

arquivo.seek(arvore_aux.pagina_raiz)
pagina_raiz.escreve_pagina(arquivo)

pagina1.chaves[0].set_pos_pagina_menor_chave(arquivo.seek(0, 2))
pagina3.set_ponteiro_pai(pagina_raiz.chaves[0].pos_pagina_menor_chave)
pagina3.escreve_pagina(arquivo)
pagina1.chaves[1].set_pos_pagina_menor_chave(arquivo.seek(0, 2))
pagina4.set_ponteiro_pai(pagina_raiz.chaves[0].pos_pagina_menor_chave)
pagina4.escreve_pagina(arquivo)
pagina1.chaves[2].set_pos_pagina_menor_chave(arquivo.seek(0, 2))
pagina5.set_ponteiro_pai(pagina_raiz.chaves[0].pos_pagina_menor_chave)
pagina5.escreve_pagina(arquivo)
pagina1.set_pos_pagina_maior_chave(arquivo.seek(0, 2))
pagina6.set_ponteiro_pai(pagina_raiz.chaves[0].pos_pagina_menor_chave)
pagina6.escreve_pagina(arquivo)
pagina2.chaves[0].set_pos_pagina_menor_chave(arquivo.seek(0, 2))
pagina7.set_ponteiro_pai(pagina_raiz.pos_pagina_maior_chave)
pagina7.escreve_pagina(arquivo)
pagina2.chaves[1].set_pos_pagina_menor_chave(arquivo.seek(0, 2))
pagina8.set_ponteiro_pai(pagina_raiz.pos_pagina_maior_chave)
pagina8.escreve_pagina(arquivo)
pagina2.set_pos_pagina_maior_chave(arquivo.seek(0, 2))
pagina9.set_ponteiro_pai(pagina_raiz.pos_pagina_maior_chave)
pagina9.escreve_pagina(arquivo)
arquivo.seek(pagina_raiz.chaves[0].pos_pagina_menor_chave)
pagina1.escreve_pagina(arquivo)
arquivo.seek(pagina_raiz.pos_pagina_maior_chave)
pagina2.escreve_pagina(arquivo)

"""TESTANDO SE ESTÁ LENDO AS PAGINAS > OK"""
arquivo.seek(0, 0)
arvore_aux = arvore.le_arvore(arquivo)
print("Lendo informações básicas da árvore:")
print(" - número de máximo de chaves por página: " + str(arvore_aux.qtd_chaves_pagina))
print(" - posição no arquivo de onde está a raiz da árvore: " + str(arvore_aux.pagina_raiz))

pagina = Pagina()
limitador = arquivo.seek(0, 2)
arquivo.seek(arvore_aux.pagina_raiz)
while pagina:
	aux = arquivo.tell()
	if aux == limitador:
	    break
	pagina_aux = pagina.le_pagina(arquivo)
	print("\nQuantidades de chaves nesta página: " + str(pagina_aux.qtd_chaves))
	for i in range(0, int(pagina_aux.qtd_chaves)):
	    print("Local da chave menor: " + str(pagina_aux.chaves[i].pos_pagina_menor_chave))
	    print("Chave: " + str(pagina_aux.chaves[i].chave))
	print("Página com chave maior: " + str(pagina_aux.pos_pagina_maior_chave))
	print("Página pai: " + str(pagina_aux.ponteiro_pai))

arquivo.close()