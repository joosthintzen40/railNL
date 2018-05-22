# RailNL
# Random Algorithm

# Import
import csv
from random import randint
import random

# Configuration
amount_of_trains = 5

# Load CSV
with open('ConnectiesHolland_test.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile))

# New dict for all connections
totaal = []

# Temp variable
temp_dict = 0

# Loading data in totaal
for i in data:
    totaal.append({"Begin":data[temp_dict][0], "Eind":data[temp_dict][1], "Tijd":data[temp_dict][2]})
    totaal.append({"Begin":data[temp_dict][1], "Eind":data[temp_dict][0], "Tijd":data[temp_dict][2]})
    temp_dict += 1

# Random start station
random_start = totaal[randint(0, (len(totaal)-1))]["Begin"]

# Loading start station with all possible connections
def connection(random_start):

    # Temp array and temp variable
    temp_array = []
    temp = 0

    # Load connection in temp_array
    for i in totaal:
        if i["Begin"] == random_start:
            temp_array.append({"Begin":totaal[temp]["Begin"],
                                "Eind":totaal[temp]["Eind"],
                                "Tijd":int(totaal[temp]["Tijd"])})

        temp += 1

    # Return traject
    traject = temp_array[randint(0, (len(temp_array)-1))]
    return traject

# Array
dienstregeling = [[],[],[],[],[],[],[]]

# Create 5 trains
for i in range(amount_of_trains):
    # print ""
    # print "Train %s" %(i + 1)
    br = 0
    time = 0
    score = 0

    # Create a single train with random connections
    while True:
        connect = connection(random_start)
        random_start = connect["Eind"]
        time += connect["Tijd"]
        br += 1

        # Break if traject is longer then 120 min
        if time > 120:
            break

        # Random break after 4 connection to create shorter trajects sometimes
        if br > 4:
            if 0.9 < random.uniform(0, 1):
                break

        # print connect
        score += connect["Tijd"]
        dienstregeling[i].append(connect)

    # print "Total time = %i" %(score)

##### Minutes & P score #####

a = 0
total_minutes = 0
check = totaal

for i in dienstregeling:

    minute = 0
    b = 0

    for j in dienstregeling[a]:

        minute += dienstregeling[a][b]["Tijd"]
        begin = dienstregeling[a][b]["Begin"]
        begin = dienstregeling[a][b]["Eind"]

        b += 1
        c = 0

        for k in check:
            # print check[c]
            c += 1

    total_minutes += minute
    a += 1

print check
# print dienstregeling[0]

# Score function
# Traject_score = (p * 10000 - ((amount_of_trains * 20) + (total_minutes / 10)))
# print Traject_score
