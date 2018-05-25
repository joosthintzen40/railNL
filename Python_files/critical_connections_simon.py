import csv

check_list = []

<<<<<<< HEAD
with open('C:/Users/Koos Hintzen/Documents/GitHub/railNL/railNL/Data/ConnectiesHolland.csv', 'r') as csvfile:
=======
with open('C:/Users/TU Delf SID/Documents/GitHub/railNL/Data/ConnectiesHolland.csv', 'r') as csvfile:
>>>>>>> 306fa815bffb5e01b8c45c8d2d0cc5a30fe92e76
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
