import csv

check_list = []

with open('C:/Users/TU Delf SID/Documents/GitHub/railNL/Data/ConnectiesNationaal.csv', 'r') as csvfile:
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
