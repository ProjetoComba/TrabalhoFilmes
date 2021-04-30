import csv

def media_count_rating(HashTableMediaCount, M, HashTable_User):
    with open('rating.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        csv_reader.__next__()

        for row in csv_reader:
            userID = int(row[0])
            movieID = int(row[1])
            rating = float(row[2])
            tupla = (movieID, rating)

            HashTable_User[userID].append(tupla)
            HashTableMediaCount[movieID][0] += rating
            HashTableMediaCount[movieID][1] += 1

        for i in range(M):
            if (HashTableMediaCount[i][0] != 0):
                HashTableMediaCount[i][0] = round(HashTableMediaCount[i][0] / HashTableMediaCount[i][1], 6)

        return HashTableMediaCount, HashTable_User
