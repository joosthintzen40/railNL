# RailNL
# Greedy Algorithm

# Import
import csv

# Load CSV
with open('ConnectiesHolland_test.csv', 'rb') as csvfile:
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

# Temp array and temp variable
temp_array = []
temp = 0

# Loading start station with all possible connections
for i in totaal:
    if i["Begin"] == 'Castricum':
        temp_array.append({"Begin":totaal[temp]["Begin"],
                            "Eind":totaal[temp]["Eind"],
                            "Tijd":int(totaal[temp]["Tijd"])})
    temp += 1

# Fastest time variable and count variable
lowest = 120
count = 0
traject = []

# Check for fastest connection
for i["Tijd"] in temp_array:
    # last = i["Tijd"]["Begin"]
    if i["Tijd"]["Tijd"] < lowest:
        # if last != i["Tijd"]["Eind"]:
            lowest = i["Tijd"]["Tijd"]
            closest = i["Tijd"]

print closest
# print last
