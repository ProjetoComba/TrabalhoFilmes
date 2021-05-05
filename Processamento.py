from Leitura_Rating import media_count_rating
from Leitura_Movies import movies_dados
from Leitura_Tags import tags
import Busca_Nome

def preProcessamento(HashTableMediaCount, HashTable_User, HashTableMovies, HashTableTags, M, root):
    HashTableMediaCount, HashTable_User = media_count_rating(HashTableMediaCount, M, HashTable_User)

    HashTableMovies = movies_dados(HashTableMovies)

    for i in range(1, M):
        if (HashTableMovies[i][0] != ''):
            Busca_Nome.add(root, HashTableMovies[i][0], i)

    HashTableTags = tags(HashTableTags)
