# Arvore B em Arquivo - Python
Código em Python da estrutura Arvore B com leitura e escrita em arquivo.

O código se divide em dois arquivos principais:
- arvore_b_struct.py (estrutura dos objetos da árvore)
- arvore_b_util.py (funções utéis da árvore: busca, inserção, remoção, impressão da árvore)

## Estrutura
Arquivo arvore_b_struct.py

Está definidas as estruturas da árvore:
- arvore
- pagina
- chave

#### Arvore
Estrutura do objeto arvore é composto de:
- número máximo de chaves por página
- ponteiro para a posição da página raiz na árvore

#### Página
Estrutura do objeto pagina é composto por:
- número de chaves presentes na página
- coleção de objetos chaves
- ponteiro para a posição da página com chave de MAIOR valor
- ponteiro para a posição da página pai, facilitando o split

#### Chave
Estrutura do objeto chave é composto por:
- possui a chave propriamente dita, que deve ser única e identifica o objeto chave
- ponteiro para a posição para encontrar a informação necessário no arquivo que foi mapeado
- ponteiro para a posição para a página com chaves de MENOR valor do que a chave atual

## Funções Úteis
Arquivo arvore_b_utils.py

Define as funções:
- busca pela chave
- inserção de objeto chave (a implementar)
- remoção de objeto chave (a implementar)
- impressão de objeto chave (a implementar)

### Busca pela chave (valor)
A função busca_arvore lê o arquivo onde está escrita a árvore e responde se a chave indicada está ou não na árvore. Recebe três parâmetros:

1.**Chave:**

O valor da chave a ser buscada, não é o objeto chave, e sim o valor da chave.

2.**Posição no arquivo:**

A posição para o início da busca para iniciar é importante que seja pela posição da página raiz.
Para encontrar a posição da página raiz basta efetuar a leitura da arvore que se encontra na posição
inicial do arquivo ```arquivo.seek(0)```.

3.**Arquivo:**

Deve ser passado também o arquivo onde se deve buscar.

### Inserção de Chave(objeto)
A função insere_arvore efetua a inclusão da chave dentro do local adequado na árvore e escreve no arquivo, recebe três parâmetros:

1.**Chave**

Recebe um objeto chave que deseja ser inserido na arvore.

2.**Ponteiro**

Para iniciar a busca o ponteiro deve ser o caminho para a página raiz da árvore.

3.**Arquivo:**

Deve ser passado também o arquivo onde se deve inserir.

### Split
É uma função auxiliar da insere_arvore que efetua o split necessário e inclui a chave na página e escreve no arquivo. Recebe três parâmetros:

1.**Pagina**

Recebe a página que deverá sofrer o split.

2.**Ponteiro**

A posição onde essa página está no arquivo.

3.**Arquivo**

Arquivo onde será escrito as novas páginas.

### Remoção de Chave(objeto)
Não implementado

### Imprime Arvore ordenada
A função imprime_arvore_ordenado faz a leitura da árvore que está no arquivo e apresenta os valores das chaves em orde crescente. Recebe somente um parâmetro, o arquivo em que se deseja ler a árvore.

### Imprime Arvore
É uma função que existe no momento apenas para facilitar o debbug do arquivo. Imprime cada uma das páginas com seus respectivos detalhes.

## Testes
No repositório também tem dois arquivos de teste:
- test_struct.py
- test_util.py

Que foram usados para teste das estruturas e utilidades.
Também consta o arquivo arvore.dat (gerado pelo test_struct.py) que contém uma árvore para testar a busca.
