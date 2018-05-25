# Hintzen, Joost - 10434143
# Heijningen, Rutger van - 10272224
# Kemmere, Simon - 10798250
#
# Function that loads in data after it was given the data.
# Data that gets loaded in depends on the configuration chosen in
# main.py.

import csv

# load in data corresponding to map, i.e. North or NL
def load_map(data):

    # Load CSV
    with open(data, 'r') as csvfile:
        data = list(csv.reader(csvfile))

    # New dict for all connections
    totaal = []

    # Temp variable
    temp_dict = 0

    # Loading data in totaal
    for i in data:
        totaal.append({"Begin":data[temp_dict][0], "Eind":data[temp_dict][1], "Tijd":data[temp_dict][2], "M":temp_dict})
        totaal.append({"Begin":data[temp_dict][1], "Eind":data[temp_dict][0], "Tijd":data[temp_dict][2], "M":temp_dict})
        temp_dict += 1

    return totaal
