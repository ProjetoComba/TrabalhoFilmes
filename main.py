import Busca_Nome
from Processamento import preProcessamento
from Pesquisa_1 import pesquisaMovie
from Pesquisa_2 import pesquisaUser
from Pesquisa_3 import pesquisaGenero
from Pesquisa_4 import pesquisaTags
import re

M = 131263 #Tamanho tabela Hash
N = 138494 #Numero de usuarios
HashTableMediaCount = [[0.0, 0] for _ in range(M)]  # INICIALIZANDO A TABELA
HashTableMovies = [['', ''] for _ in range(M)]  # INICIALIZANDO A TABELA
HashTable_User = [[] for _ in range(N)]
HashTableTags = [[] for _ in range(M)]
root = Busca_Nome.TrieNode('*')

preProcessamento(HashTableMediaCount, HashTable_User, HashTableMovies, HashTableTags, M, root)


while (True):
    entrada = str(input("$ ")).split(" ", 1)

    op = entrada[0].upper()
    entrada.pop(0)

    if (op == 'MOVIE'):
        nome = entrada[0]
        pesquisaMovie(nome, root, HashTableMovies, HashTableMediaCount)
    elif (op == 'USER'):
        usuario = int(entrada[0])
        print(usuario)
        pesquisaUser(usuario, HashTable_User, HashTableMovies, HashTableMediaCount)
    elif (re.split('(\d+)', op)[0] == 'TOP'):
        topN = int(re.split('(\d+)', op)[1])
        genero = entrada[0].upper().replace("'", "")
        print(topN, genero)
        pesquisaGenero(topN, genero, M, HashTableMovies, HashTableMediaCount)
    elif (op == 'TAG'):
        listaTags = entrada[0].upper().split(" '")
        print(listaTags)
        pesquisaTags(listaTags, M, HashTableMovies, HashTableTags, HashTableMediaCount)
    else:
        print("Comando inválido\nDigite um comando válido para pesquisa")
