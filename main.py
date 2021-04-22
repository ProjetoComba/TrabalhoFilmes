import csv

def media_count_rating(HashTableMediaCount, M):
    with open('rating.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        csv_reader.__next__()

        for row in csv_reader:
            movieID = int(row[1])
            rating = float(row[2])

            HashTableMediaCount[movieID][0] += rating
            HashTableMediaCount[movieID][1] += 1

        for i in range(M):
            if (HashTableMediaCount[i][0] != 0):
                HashTableMediaCount[i][0] = round(HashTableMediaCount[i][0] / HashTableMediaCount[i][1], 6)

        return HashTableMediaCount



def movies_dados(HashTableMovies):
##### salvando os dados dos filmes em uma tabela hash ######
    with open('movie_clean.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        csv_reader.__next__()

        for row in csv_reader:
            movieID = int(row[0])
            nome = str(row[1])
            genero = str(row[2])

            HashTableMovies[movieID][0] = nome
            HashTableMovies[movieID][1] = genero

        return HashTableMovies

########### BUSCA DE NOME ########################
class TrieNode(object):

    def __init__(self, char: str, movieid=0):
        self.char = char
        self.children = []
        self.movieid = 0
        self.word_finished = False
        self.counter = 1
        self.folha = False


def add(root, word: str, movieid: int):

    node = root
    for char in word:
        found_in_child = False

        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child

                if node.folha == True:
                    node.folha = False

                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)

            node = new_node

    if len(node.children) == 0:
        node.folha = True

    node.movieid = movieid # Adiciona o campo movieID no ultimo caracter adicionado na arvore trie
    node.word_finished = True


def find_prefix(root, prefix: str):

    node = root

    if not root.children:
        return False, 0

    for char in prefix:
        char_not_found = True

        for child in node.children:
            if child.char == char:

                char_not_found = False

                node = child
                break

        if char_not_found:
            return False, 0

    return True, node


def acha_o_resto (node, achados):

    if (node.movieid != 0):
        achados.append(node.movieid)
        if (node.folha == True):
            return

    for child in node.children:

        if (child.folha == True):
            achados.append(child.movieid)
            break

        if (child.counter != 0 ):
            aux = acha_o_resto(child, achados)
            if aux != 0:
                achados.append(aux)

    return child.movieid


################### MAIN ############################
M = 131263
HashTableMediaCount = [[0.0, 0] for _ in range(M)]  # INICIALIZANDO A TABELA

HashTableMediaCount = media_count_rating(HashTableMediaCount, M)

# for i in range(1, M):
#     if (HashTableMediaCount[i][0] != 0):
#         print(i, HashTableMediaCount[i])

HashTableMovies = [['', ''] for _ in range(M)]  # INICIALIZANDO A TABELA

HashTableMovies = movies_dados(HashTableMovies)

if __name__ == "__main__":
    root = TrieNode('*')
    achados= []

    for i in range(1, M):
        if (HashTableMovies[i][0] != ''):
            add(root, HashTableMovies[i][0], i)

    while(True):
        print("Digite o nome do filme que deseja buscar: ")
        nome = input()

        tupla = (find_prefix(root, nome))

        if tupla[0] == True:
            acha_o_resto(tupla[1], achados)

        achados = sorted(set(achados))

        for id in achados:
            print(f"{id}, {' , '.join(map(str, HashTableMovies[id]))} , {' , '.join(map(str, HashTableMediaCount[id]))}")
