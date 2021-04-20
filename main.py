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


######## main #########
M = 131263
HashTableMediaCount = [[0.0, 0] for _ in range(M)]  # INICIALIZANDO A TABELA

HashTableMediaCount = media_count_rating(HashTableMediaCount, M)

for i in range(1, M):
    if (HashTableMediaCount[i][0] != 0):
        print(i, HashTableMediaCount[i])

HashTableMovies = [['', ''] for _ in range(M)]  # INICIALIZANDO A TABELA

HashTableMovies = movies_dados(HashTableMovies)

for i in range(1, M):
    if (HashTableMovies[i][0] != ''):
        print(f"{i}, {' , '.join(map(str, HashTableMovies[i]))} , {' , '.join(map(str, HashTableMediaCount[i]))}")
