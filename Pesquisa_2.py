
def pesquisaUser(usuario, HashTable_User, HashTableMovies, HashTableMediaCount):
    for movie in HashTable_User[usuario]:
        print(f"{movie[1]}, {str(HashTableMovies[movie[0]][0])} , {' , '.join(map(str, HashTableMediaCount[movie[0]]))}")
