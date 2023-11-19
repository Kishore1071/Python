import csv

d = csv.reader(open('City.csv'))

for row in d:

    print(row)

    for a in row:

        print(a)