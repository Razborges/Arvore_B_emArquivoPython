#Arvore B em Arquivo - Python
Código em Python da estrutura Arvore B com leitura e escrita em arquivo.

O código se divide em dois arquivos principais:
- arvore_b_struct.py (estrutura dos objetos da árvore)
- arvore_b_util.py (funções utéis da árvore: busca, inserção, remoção, impressão da árvore)

##Estrutura
Arquivo arvore_b_struct.py

Está definidas as estruturas da árvore:
- arvore
- pagina
- chave

####Arvore
Estrutura do objeto arvore é composto de:
- número máximo de chaves por página
- ponteiro para a posição da página raiz na árvore

####Pagina
Estrutura do objeto pagina é composto por:
- número de chaves presentes na página
- coleção de objetos chaves
- ponteiro para a posição da página com chave de MAIOR valor

####Chave
Estrutura do objeto chave é composto por:
- possui a chave propriamente dita, que deve ser única e identifica o objeto chave
- ponteiro para a posição para encontrar a informação necessário no arquivo que foi mapeado
- ponteiro para a posição para a página com chaves de MENOR valor do que a chave atual

##Funções Úteis
Arquivo arvore_b_utils.py

Define as funções:
- busca pela chave
- inserção de objeto chave (a implementar)
- remoção de objeto chave (a implementar)
- impressão de objeto chave (a implementar)

###Busca pela chave (valor)
A função busca_arvore recebe três parâmetros:

1.**Chave:**

O valor da chave a ser buscada, não é o objeto chave, e sim o valor da chave.

2.**Posição no arquivo:**

A posição para o início da busca para iniciar é importante que seja pela posição da página raiz.
Para encontrar a posição da página raiz basta efetuar a leitura da arvore que se encontra na posição
inicial do arquivo ```arquivo.seek(0)```.

3.**Arquivo:**

Deve ser passado também o arquivo onde se deve buscar.

###Inserção de Chave(objeto) --- Apresentando ERRO no lado Maior da Raiz
A função insere_arvore recebe três parâmetros:

1.**Chave**

Recebe um objeto chave que deseja ser inserido na arvore.

2.**Ponteiro**

Para iniciar a busca o ponteiro deve ser o caminho para a página raiz da árvore.

3.**Arquivo:**

Deve ser passado também o arquivo onde se deve inserir.

###Remoção de Chave(objeto)
Não implementado

###Imprime Arvore ordenada
A função imprime_arvore_ordenado recebe somente um parâmetro, o arquivo que se deseja buscar a árvore e os valores que lá estão.

###Imprime Arvore
É uma função que existe no momento apenas para facilitar o debbug do arquivo.

##Testes
No repositório também tem dois arquivos de teste:
- test_struct.py
- test_util.py

Que foram usados para teste das estruturas e utilidades.
Também consta o arquivo arvore.dat (gerado pelo test_struct.py) que contém uma árvore para testar a busca.
