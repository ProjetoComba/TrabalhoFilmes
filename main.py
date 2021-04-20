import csv

#TESTE GIT HUB

M = 131263
HashTableMediaCount = [[0.0, 0] for _ in range(M)]  # INICIALIZANDO A TABELA

with open('rating.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_reader.__next__()


    for row in csv_reader:
        movieID = int(row[1])
        rating = float(row[2])

        HashTableMediaCount[movieID][0] += rating
        HashTableMediaCount[movieID][1] += 1

    for i in range(M):
        if(HashTableMediaCount[i][0] != 0):
            HashTableMediaCount[i][0] = round(HashTableMediaCount[i][0]/HashTableMediaCount[i][1], 6)

aux = 0
for i in range(1, M):
    if (HashTableMediaCount[i][0] != 0):
        print(i, HashTableMediaCount[i])
        aux += 1

print(aux)