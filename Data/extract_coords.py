import csv

xcoord = []
ycoord = []
with open('StationsNationaal.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for coordinate in csvreader:
        xcoord.append(coordinate[1])
        ycoord.append(coordinate[2])

print (xcoord)
