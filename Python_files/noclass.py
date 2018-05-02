import csv

nlreader = {}

with open('ConnectiesHolland.csv', 'r') as csvfile:
      nlreader = csv.reader(csvfile)
      print(nlreader)
      # for row in nlreader:
      #     g.add_station(row[0])
      #     g.add_station(row[1])
      #     g.add_connection(row[0], row[1], int(row[2]))
