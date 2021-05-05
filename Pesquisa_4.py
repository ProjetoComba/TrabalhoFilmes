
def pesquisaTags(listaTags, M, HashTableMovies, HashTableTags, HashTableMediaCount):
    Tabela_Tags = []        # TABELA DOS FILMES A SEREM EXIBIDOS PARA AS TAGS DIGITADAS

    for i in range (len(listaTags)):
        listaTags[i] = listaTags[i].replace("'", "")

    setAuxTagsDigitadas = set(listaTags)  # AUXILIARES POIS PARA A COMPARAÇÃO DE INTERSECÇÃO PRECISAM SER SETS

    for i in range(1, M):
        if (HashTableMovies[i][1] != ''):
            setAuxTagsArquivo = set(HashTableTags[i])

            if setAuxTagsDigitadas.intersection(setAuxTagsArquivo) == setAuxTagsDigitadas:
                Tabela_Tags.append(i)


    for i in range (len(Tabela_Tags)):
        movieId = Tabela_Tags[i]
        print(f"{' , '.join(map(str, HashTableMovies[movieId]))} , {' , '.join(map(str, HashTableMediaCount[movieId]))}")
