from Ordenamento import quick_sort
from Leitura_Rating import media_count_rating
from Leitura_Movies import movies_dados
import Busca_Nome
import re

################### MAIN ############################
M = 131263 #Tamanho tabela Hash
N = 138494 #Numero de usuarios
HashTableMediaCount = [[0.0, 0] for _ in range(M)]  # INICIALIZANDO A TABELA
HashTable_User = [[] for _ in range(N)]

HashTableMediaCount, HashTable_User = media_count_rating(HashTableMediaCount, M, HashTable_User)

HashTableMovies = [['', ''] for _ in range(M)]  # INICIALIZANDO A TABELA

HashTableMovies = movies_dados(HashTableMovies)

##### CHAMADA PESQUISA 2.1 #############
usuario = int(input("Digite o usuario: "))
for movie in HashTable_User[usuario]:
    print(f"{movie[1]}, {str(HashTableMovies[movie[0]][0])} , {' , '.join(map(str, HashTableMediaCount[movie[0]]))}")
print("#"*50)

##### CHAMADA PESQUISA 2.2 #############
if __name__ == "__main__":
    root = Busca_Nome.TrieNode('*')
    achados = []

    for i in range(1, M):
        if (HashTableMovies[i][0] != ''):
            Busca_Nome.add(root, HashTableMovies[i][0], i)

    while(True):
        achados.clear()

        print("Digite o nome do filme que deseja buscar: ")
        nome = input()

        if nome == '-1':
            break

        tupla = (Busca_Nome.find_prefix(root, nome))

        if tupla[0] == True:
            Busca_Nome.acha_o_resto(tupla[1], achados)

        achados = sorted(set(achados))

        for id in achados:
            print(f"{id}, {' , '.join(map(str, HashTableMovies[id]))} , {' , '.join(map(str, HashTableMediaCount[id]))}")

##### CHAMADA PESQUISA 2.3 #############
Table_Generos = []        # TAMANHO TABELA GENEROS

entradaGeneros = str(input("Digite o topX e o gênero: ")).upper().split()

topN = int(re.sub('[^0-9]','', entradaGeneros[0]))

genero = entradaGeneros[1].replace("'", "")

for i in range(1, M):
    if (HashTableMovies[i][1] != ''):
        if ((genero in (HashTableMovies[i][1]).upper()) and (HashTableMediaCount[i][1] >= 1000)):
            tuplaAux = (HashTableMediaCount[i][0], i)

            Table_Generos.append(tuplaAux)

quick_sort(Table_Generos, len(Table_Generos))
Table_Generos.reverse()

for i in range (0, topN):
    movieId = Table_Generos[i][1]
    print(f"{' , '.join(map(str, HashTableMovies[movieId]))} , {' , '.join(map(str, HashTableMediaCount[movieId]))}")
