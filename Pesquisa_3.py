from Ordenamento import quick_sort

def pesquisaGenero(topN, genero, M, HashTableMovies, HashTableMediaCount):
    Table_Generos = []        # TABELA GENEROS

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
