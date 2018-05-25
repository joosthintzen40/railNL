import csv

check_list = []

with open('C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/ConnectiesHolland.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for connection in csvreader:
        lists = []
        listrev = []
        lists.append(connection[0])
        lists.append(connection[1])
        check_list.append(lists)
        listrev.append(connection[1])
        listrev.append(connection[0])
        check_list.append(listrev)
