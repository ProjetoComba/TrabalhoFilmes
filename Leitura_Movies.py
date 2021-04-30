import csv

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
