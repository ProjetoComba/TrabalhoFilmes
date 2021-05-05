import csv

def tags(HashTableTags):
    with open('tag_clean.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        csv_reader.__next__()

        for row in csv_reader:
            movieID = int(row[1])
            tag = str(row[2]).upper()

            HashTableTags[movieID].append(tag)

        return HashTableTags
